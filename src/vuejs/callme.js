Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-seller',
    delimiters: ['[[', ']]'],
    data: {
        affordablelands: [],
        loading: false,
        saving: false,
        currentAffordableLands: {},
        customerCareSpecialist: [],
        message: null,
        newAffordableLands: {
            'call_date': null,
            'customer_care_specialist': '',
            'contact_information': '',
            'name': '',
            'state_county': '',
            'parcel_number': '',
            'property_owner': '',
            'other_owners': '',
            'sell_the_property': '',
            'phone_number': '',
            'email_address': '',
            'listed_in_letter_or_postcard': '',
            'for_your_property': '',
            'average_handling_time': null,
            'additional_notes': '',
        },
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
        this.getAffordableLandInvestment();
        this.getCustomerCareSpecialist();
    },
    methods: {
        reset: function () {
            Object.keys(this.newAffordableLands).forEach(key => {
                this.newAffordableLands[key] = ""
            })
        },
        getAffordableLandInvestment: function () {
            this.loading = true;
            this.$http.get(`/api/v1/affordable-land/`)
                .then((response) => {
                    this.loading = false;
                    this.affordablelands = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getCustomerCareSpecialist: function () {
            this.loading = true;
            this.$http.get(`/api/v1/customer-care-specialist/`)
                .then((response) => {
                    this.customerCareSpecialist = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        searchMonthCashOut: function () {
            this.loading = true;
            this.$http.get(`/api/v1/cashout/?date_release__month=${this.search_month}`)
                .then((response) => {
                    this.loading = false;
                    this.cashouts = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addAffordableLand: function () {
            this.saving = true;
            this.$http.post('/api/v1/affordable-land/', this.newAffordableLands)
                .then((response) => {
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: "Affordable Land Investment data has been added successfully",
                        icon: "success",
                        buttons: false,
                        timer: 2000
                    })
                    this.reset();
                })
                .catch((err) => {
                    this.loading = false;
                    swal({
                        title: "GPG System",
                        text: JSON.stringify(err.body),
                        icon: "error",
                        buttons: "Ok",
                    });
                    console.log(err);
                })
        },
        getPaginatedRecords: function () {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.cashouts.slice().splice(startIndex, this.pageSize);
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
        cashouts: function (newCashOutRecords, oldCashOutRecords) {
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
            return this.cashouts.length;
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
    }
});
