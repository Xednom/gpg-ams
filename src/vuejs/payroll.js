Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-payroll',
    delimiters: ['[[', ']]'],
    data: {
        payrolls: [],
        loading: false,
        currentPayroll: {},
        message: null,
        newPayroll: {
            'date': null,
            'virtual_assistant': null,
            'time_in': null,
            'time_out': null,
            'hours': null,
            'client_name': null,
            'rate': null,
            'salary': null,
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
        // this.getPayroll();
        this.setCurrentMonth();
        this.searchMonthPayroll();
    },
    methods: {
        setCurrentMonth: function () {
            let currentMonth = moment(new Date()).format("MM");
            this.search_month = currentMonth;
            console.log(currentMonth);
        },
        getPayroll: function () {
            this.loading = true;
            this.$http.get(`/api/v1/payroll/`)
                .then((response) => {
                    this.loading = false;
                    this.payrolls = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        searchMonthPayroll: function () {
            this.loading = true;
            this.$http.get(`/api/v1/payroll/?date__month=${this.search_month}`)
                .then((response) => {
                    this.loading = false;
                    this.payrolls = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getPaginatedRecords: function () {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.payrolls.slice().splice(startIndex, this.pageSize);
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
        payrolls: function (newPayrollRecords, oldPayrollRecords) {
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
            return this.payrolls.length;
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
        totalSalary: function () {
            return this.payrolls.reduce(function (sum, payrolls) {
                return sum + parseFloat(payrolls.salary);
            }, 0);
        }
    }
});
