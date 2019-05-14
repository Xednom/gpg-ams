Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-timesheet',
    delimiters: ['[[', ']]'],
    data: {
        timesheets: [],
        paymentmade: [],
        loading: false,
        currentTimeSheet: {},
        message: null,
        newTimeSheet: {
            'date': null,
            'company_tagging': null,
            'shift_date': null,
            'month_to_date': null,
            'clients_full_name': null,
            'title_job_request': null,
            'job_request': null,
            'time_in': null,
            'time_out': null,
            'duration': null,
            'total_items': null,
            'additional_comments': null,
            'assigned_job_request_to': null,
            'hourly_rate': null,
            'amount_charge': null,
            'tax_fee': null,
            'total_tax_fee': null,
            'total_amount_due': null,
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
        this.searchMonthTimeSheet();
    },
    methods: {
        setCurrentMonth: function () {
            let currentMonth = moment(new Date()).format("MM");
            this.search_month = currentMonth;
        },
        getTimeSheet: function () {
            this.loading = true;
            this.$http.get(`/api/v1/timesheet/`)
                .then((response) => {
                    this.loading = false;
                    this.timesheets = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        searchAll: function () {
            this.searchMonthTimeSheet();
            this.searchMonthPaymentMade();
        },
        searchMonthTimeSheet: function () {
            this.loading = true;
            this.$http.get(`/api/v1/timesheet/?shift_date__month=${this.search_month}`)
                .then((response) => {
                    this.loading = false;
                    this.timesheets = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        searchMonthPaymentMade: function () {
            this.loading = true;
            this.$http.get(`/api/v1/paymentmade/?date__month=${this.search_month}`)
                .then((response) => {
                    this.loading = false;
                    this.paymentmade = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getPaymentMade: function () {
            this.loading = true;
            this.$http.get(`/api/v1/paymentmade`)
                .then((response) => {
                    this.loading = false;
                    this.paymentmade = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
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
        totalDue: function () {
            let sum = this.totalTimeSheet - this.totalpaymentmade;
            return sum.toFixed(2);
        }
    }
});
