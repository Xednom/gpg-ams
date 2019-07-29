Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
new Vue({
    el: '#gpg-timesheet',
    delimiters: ['[[', ']]'],
    data: {
        timesheets: [],
        cashouts: [],
        clients: [],
        paymentmade: [],
        errortimesheet: [],
        loading: false,
        viewing: false,
        searching: false,
        saving: false,
        errored: false,
        currentTimeSheet: {},
        message: null,
        newTimeSheet: {
            'company_tagging': null,
            'shift_date': null,
            'month_to_date': null,
            'clients_full_name': null,
            'title_job_request': null,
            'channel_job_requested': null,
            'job_request_description': null,
            'time_in': null,
            'time_out': null,
            'duration': null,
            'total_items': null,
            'additional_comments': null,
            'assigned_va': null,
            'assigned_pm': null,
            'hourly_rate_peso': null,
            'hourly_rate_usd': null,
            'total_charge_peso': null,
            'total_charge_usd': null,
            'paypal_charge': null,
            'total_charge_with_paypal': null,
            'total_amount_due': null,
            'status': null,
            'admin_approval': null
        },
        search_term: '',
        search_month: '',

        // for pagination
        currentPage: 1,
        pageSize: RECORDS_PER_PAGE,
        startPage: 1,
        endPage: null,
        maxPages: RECORDS_PER_PAGE,
        paginatedRecords: [],
    },
    mounted: function () {
        this.setCurrentMonth();
        this.searchMonthPaymentMade();
        this.searchMonthVaTimeSheet();
        this.searchMonthClientTimeSheet();
        this.loadClient();
        this.searchMonthCashOut();
        this.getCashOut();
    },
    methods: {
        setCurrentMonth: function () {
            let currentMonth = moment(new Date()).format("MM");
            this.search_month = currentMonth;
        },
        getTimeSheet: function () {
            this.loading = true;
            axios.get(`/api/v1/timesheet/`)
                .then((response) => {
                    this.loading = false;
                    this.timesheets = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        getCashOut: function () {
            this.loading = true;
            axios.get(`/api/v1/cashout/`)
                .then((response) => {
                    this.loading = false;
                    this.cashouts = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        searchMonthVaTimeSheet () {
            this.searching = true;
            axios.get(`/api/v1/timesheet/?shift_date__month=${this.search_month}`)
                .then((response) => {
                    this.searching = false;
                    this.timesheets = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        searchMonthCashOut: function () {
            this.searching = true;
            axios.get(`/api/v1/cashout/?cash_date_release__month=${this.search_month}`)
                .then((response) => {
                    this.searching = false;
                    this.cashouts = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        searchAll: function () {
            this.searchMonthClientTimeSheet();
            this.searchMonthVaTimeSheet();
            this.searchMonthPaymentMade();
            this.searchMonthCashOut();
        },
        searchMonthClientTimeSheet: function () {
            this.searching = true;
            axios.get(`/api/v1/timesheet/?shift_date__month=${this.search_month}`)
                .then((response) => {
                    this.searching = false;
                    this.timesheets = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        viewTimeSheet (id) {
            this.viewing = true;
            axios.get(`/api/v1/timesheet/${id}`)
                .then((response) => {
                    this.viewing = false;
                    this.currentTimeSheet = response.data;
                })
                .catch((err) => {
                    this.viewing = false;
                    this.errored = true;
                    this.errortimesheet = err.body;
                    console.log(err.response.data);
                })
        },
        updateTimeSheet () {
            this.saving = true;
            axios.put(`/api/v1/timesheet/${this.currentTimeSheet.id}/`, this.currentTimeSheet)
                .then((response) => {
                    this.saving = false;
                    this.currentTimeSheet = response.data;
                    swal({
                        title: "GPG system",
                        text: "Successfully updated the informations!",
                        icon: "success",
                        button: false,
                        timer: 1500
                    })
                    $("#viewModal").modal('hide')
                    this.getTimeSheet();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        loadClient () {
            this.loading = true;
            axios.get(`/api/v1/clients`)
                .then((response) => {
                    this.loading = false;
                    this.clients = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    this.errored = true;
                    console.log(err.response.data);
                })
        },
        searchMonthPaymentMade () {
            this.searching = true;
            axios.get(`/api/v1/paymentmade/?date__month=${this.search_month}`)
                .then((response) => {
                    this.searching = false;
                    this.paymentmade = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        getPaymentMade: function () {
            this.loading = true;
            axios.get(`/api/v1/paymentmade`)
                .then((response) => {
                    this.loading = false;
                    this.paymentmade = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        getPaginatedRecords: function () {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.timesheets.slice().splice(startIndex, this.pageSize);
        },
        goToPage: function (page) {
            if (page < 1) {
                return this.currentPage = 1;
            }
            if (page > this.totalPages) {
                return this.currentPage = this.totalPages;
            }
            this.currentPage = page;
        },
        setPageGroup: function () {
            if (this.totalPages <= this.maxPages) {
                this.startPage = 1;
                this.endPage = Math.min(this.totalPages, this.maxPages);
            } else {
                let maxPagesBefireCurrentPage = Math.floor(this.maxPages / 2);
                let maxPagesAfterCurrentPage = Math.ceil(this.maxPages / 2) - 1;
                if (this.currentPage <= maxPagesBeforeCurrentPage) {
                    // current page near the start
                    this.startPage = 1;
                    this.endPage = this.maxPages;
                } else if (thiscurrentPage + maxPagesAfterCurrentPage >= this.totalPages) {
                    // current page near the end
                    this.startPage = this.totalPages - this.maxPages + 1;
                    this.endPage = this.totalPages;
                } else {
                    // current page somewhere in the middle
                    this.startPage = this.currentPage - maxPagesBeforeCurrentPage;
                    this.endPage = this.currentPage + maxPagesAfterCurrentPage;
                }
            }
        }
    },
    watch: {
        timesheets: function (newTimeSheetRecords, oldTimeSheetRecords) {
            this.setPageGroup();
            this.getPaginatedRecords();
        },
        currentPage: function (newCurrenPage, oldCurrentPage) {
            this.setPageGroup();
            this.getPaginatedRecords();
        },
    },
    computed: {
        totalItems: function () {
            return this.timesheets.length;
        },
        totalPages: function () {
            return Math.ceil(this.totalItems / this.pageSize);
        },
        startIndex: function () {
            return (this.currentPage - 1) * this.pageSize;
        },
        endIndex: function () {
            return Math.min(this.startIndex + this.pageSize - 1, this.totalItems - 1);
        },
        pages: function () {
            let pages = [];
            for (let i = this.startPage; i <= this.endPage; i++) pages.push(i);
            return pages;
        },
        totalTimeSheet: function () {
            return this.timesheets.reduce(function (sum, timesheets) {
                return sum + parseFloat(timesheets.total_amount_due);
            }, 0);
        },
        totalpaymentmade: function () {
            return this.paymentmade.reduce(function (sum, paymentmade) {
                return sum + parseFloat(paymentmade.amount);
            }, 0);
        },
        totalCashOut: function () {
            return this.cashouts.reduce(function (sum, cashouts) {
                return sum + parseFloat(cashouts.amount);
            }, 0);
        },
        totalCreditsLeft: function () {
            let sum = this.totalpaymentmade - this.totalTimeSheet;
            return sum.toFixed(2);
        },
        totalSalaryVa () {
            return this.timesheets.reduce(function (sum, timesheets) {
                return sum + parseFloat(timesheets.total_charge_peso)
            }, 0)
        },
        totalWorkHrs () {
            return this.timesheets.reduce(function (sum, timesheets) {
                return sum + parseFloat(timesheets.duration)
            }, 0)
        },
        totalDueStaffs () {
            let sum = this.totalSalaryVa - this.totalCashOut;
            return sum.toFixed(2);
        }
    }
});
