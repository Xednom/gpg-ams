Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
new Vue({
    el: '#gpg-landacademy',
    delimiters: ['[[', ']]'],
    data: {
        landacademy: [],
        smartpricing: [],
        staffs: [],
        clients: [],
        loading: false,
        viewing: false,
        saving: false,
        searching: false,
        message: null,
        currentLands: [],
        currentPricings: [],
        currentSort: '',
        currentSortDir: 'desc',
        newLandAcademy: {
            'date_requested': null,
            'date_completed': null,
            'date_payment_made': null,
            'order_name': null,
            'client_la_requestor': null,
            'complete_order': null,
            'status_of_order': null,
            'payment_status': null,
            'invoice': null,
            'total_items_requested': null,
            'notes': null,
        },

        newSmartPricing: {
            'situs_address': null,
            'trulia': null,
            'zillow': null,
            'redfin': null,
            'realfor': null,
            'realtytrac': null,
            'order_name': null,
            'requestor_full_name': null,
            'date_requested': null,
            'date_research': null,
            'date_encoded': null,
            'quality_check_status': null,
            'quality_specialist': null,
            'notes_from_researcher': null,
            'notes_from_qa': null,
        },
        
        // for normal search
        search_client_name: '',


        // for advanced search inventory
        advance_search_date_requested: '',
        advance_search_date_completed: '',
        advance_search_date_payment_made: '',
        advance_search_order_name: '',
        advance_search_client_la_requestor: '',
        advance_search_status_of_order: '',
        advance_search_payment_status: '',

        //for advanced search smart pricing
        search_date_requested: '',
        search_date_research: '',
        search_date_encoded: '',
        search_requestor: '',
        search_quality_check: '',

        // for pagination
        currentPage: 1,
        pageSize: RECORDS_PER_PAGE,
        startPage: 1,
        endPage: null,
        maxPages: RECORDS_PER_PAGE,
        paginatedRecords: [],
    },
    mounted: function () {
        this.getStaffs();
        this.getClients();
        this.getLandAcademy();
        this.getSmartPricing();
        this.setCurrentDate();
    },
    methods: {
        nextPage: function () {
                if ((this.currentPage * this.pageSize) < this.landacademy.length) this.currentMasterBoardPage++;
            },
            prevPage: function () {
                if (this.currentPage > 1) this.currentPage--;
            },
            sort: function (s) {
                //if s == current sort, reverse
                if (s === this.currentSort) {
                    this.currentSortDir = this.currentSortDir === 'asc' ? 'desc' : 'asc';
                }
                this.currentSort = s;
            },
        filterKey(e) {
            const key = e.key;

            // If is '.' key, stop it
            if (key === '.')
                return e.preventDefault();

            // OPTIONAL
            // If is 'e' key, stop it
            if (key === 'e')
                return e.preventDefault();
        },

        // This can also prevent copy + paste invalid character
        filterInput(e) {
            e.target.value = e.target.value.replace(/[^0-9]+/g, '');
        },
        setCurrentDate: function () {
            let currentDate = moment(new Date()).format("YYYY-MM-DD");
            this.newLandAcademy.date_requested = currentDate;
            this.newLandAcademy.date_completed = currentDate;
            this.newSmartPricing.date_requested = currentDate;
            this.newSmartPricing.date_research = currentDate;
            this.newSmartPricing.date_encoded = currentDate;
        },
        reset: function () {
            Object.keys(this.newLandAcademy).forEach(key => {
                this.newLandAcademy[key] = ""
            })
        },
        reseto2o: function () {
            Object.keys(this.newSmartPricing).forEach(key => {
                this.newSmartPricing[key] = ""
                this.setCurrentDate();
            })
        },
        getLandAcademy: function () {
            this.loading = true;
            axios.get(`/api/v1/landacademy-inventory/`)
                .then((response) => {
                    this.loading = false;
                    this.landacademy = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        getSmartPricing: function () {
            this.loading = true;
            axios.get(`/api/v1/o2o-smart-pricing/`)
                .then((response) => {
                    this.loading = false;
                    this.smartpricing = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        viewLandAcademy: function (id) {
            this.viewing = true;
            axios.get(`/api/v1/landacademy-inventory/${id}/`)
                .then((response) => {
                    this.viewing = false;
                    this.currentLands = response.data;
                })
                .catch((err) => {
                    this.viewing = false;
                    console.log(err.response.data);
                })
        },
        viewSmartPricing: function (id) {
            this.viewing = true;
            axios.get(`/api/v1/o2o-smart-pricing/${id}/`)
                .then((response) => {
                    this.viewing = false;
                    this.currentPricings = response.data;
                })
                .catch((err) => {
                    this.viewing = false;
                    console.log(err.response.data);
                })
        },
        getStaffs: function () {
            this.loading = true;
            axios.get(`/api/v1/staffs/`)
                .then((response) => {
                    this.staffs = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        getClients: function () {
            this.loading = true;
            axios.get(`/api/v1/clients-callme/`)
                .then((response) => {
                    this.clients = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        addLandAcademy: function () {
            this.saving = true;
            axios.post('/api/v1/landacademy-inventory/', this.newLandAcademy)
                .then((response) => {
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: "Land Academy informations has been added successfully! You can add another one.",
                        icon: "success",
                        buttons: false,
                        timer: 3000
                    })
                    this.reset();
                })
                .catch((err) => {
                    this.saving = false;
                    this.errored = true;
                    swal({
                        title: "GPG System",
                        text: "Please check the summaries of your request. If the problem persist, please contact the admin.",
                        icon: "error",
                        buttons: "Ok",
                    })
                    console.log(err.response.data);
                })
        },
        addSmartPricing: function () {
            this.saving = true;
            axios.post('/api/v1/o2o-smart-pricing/', this.newSmartPricing)
                .then((response) => {
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: "O2O Smart Pricing informations has been added successfully! You can add another one.",
                        icon: "success",
                        buttons: false,
                        timer: 3000
                    })
                    this.reseto2o();
                })
                .catch((err) => {
                    this.saving = false;
                    this.errored = true;
                    swal({
                        title: "GPG System",
                        text: "Please check the summaries of your request. If the problem persist, please contact the admin.",
                        icon: "error",
                        buttons: "Ok",
                    })
                    console.log(err.response.data);
                })
        },
        updateLandAcademy: function () {
            this.saving = true;
            axios.put(`/api/v1/landacademy-inventory/${this.currentLands.id}/`, this.currentLands)
                .then((response) => {
                    this.saving = false;
                    this.currentLands = response.data;
                    swal({
                        title: "GPG system",
                        text: "Successfully updated the informations!",
                        icon: "success",
                        button: false,
                        timer: 1500
                    })
                    $("#editModal").modal('hide')
                    this.getLandAcademy();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        updateSmartPricing: function () {
            this.saving = true;
            axios.put(`/api/v1/o2o-smart-pricing/${this.currentPricings.id}/`, this.currentPricings)
                .then((response) => {
                    this.saving = false;
                    this.currentPricings = response.data;
                    swal({
                        title: "GPG system",
                        text: "Successfully updated the informations!",
                        icon: "success",
                        button: false,
                        timer: 1500
                    })
                    $("#editModal").modal('hide')
                    this.getBoard();
                })
                .catch((err) => {
                    this.saving = false;
                    console.log(err.response.data);
                })
        },
        normalSearchLandAcademy: function () {
            this.searching = true;
            axios.get(`/api/v1/landacademy-inventory/?client_la_requestor=${this.search_client_name}`)
                .then((response) => {
                    this.searching = false;
                    this.landacademy = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        normalSearchSmartPricing: function () {
            this.searching = true;
            axios.get(`/api/v1/o2o-smart-pricing/?requestor_full_name=${this.search_requestor}`)
                .then((response) => {
                    this.searching = false;
                    this.smartpricing = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        advanceSearchLandAcademy: function () {
            this.searching = true;
            axios.get(`/api/v1/landacademy-inventory/?date_requested=${this.advance_search_date_requested}&date_completed=${this.advance_search_date_completed}&date_payment_made=${this.advance_search_date_payment_made}&client_la_requestor=${this.advance_search_client_la_requestor}&status_of_order=${this.advance_search_status_of_order}&payment_status=${this.advance_search_payment_status}&order_name=${this.advance_search_order_name}`)
                .then((response) => {
                    this.searching = false;
                    this.landacademy = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        advanceSearchSmartPricing: function () {
            this.searching = true;
            axios.get(`/api/v1/o2o-smart-pricing/?date_requested=${this.search_date_requested}&date_research=${this.search_date_research}&date_encoded=${this.search_date_encoded}&requestor_full_name=${this.search_requestor}&quality_check_status=${this.search_quality_check}`)
                .then((response) => {
                    this.searching = false;
                    this.smartpricing = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        getPaginatedRecords: function () {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.landacademy.slice().splice(startIndex, this.pageSize);
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
                let maxPagesBeforeCurrentPage = Math.floor(this.maxPages / 2);
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
        landacademy: function (newLandAcademyRecords, oldlandacademyRecords) {
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
            return this.landacademy.length;
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
        sortedLandAcademy: function () {
            return this.landacademy.sort((a, b) => {
                let modifier = 1;
                if (this.currentSortDir === 'desc') modifier = -1;
                if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
                if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
                return 0;
            }).filter((row, index) => {
                let start = (this.currentPage - 1) * this.pageSize;
                let end = this.currentPage * this.pageSize;
                if (index >= start && index < end) return true;
            });
        },
        sortedSmartPricing: function () {
            return this.smartpricing.sort((a, b) => {
                let modifier = 1;
                if (this.currentSortDir === 'desc') modifier = -1;
                if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
                if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
                return 0;
            }).filter((row, index) => {
                let start = (this.currentPage - 1) * this.pageSize;
                let end = this.currentPage * this.pageSize;
                if (index >= start && index < end) return true;
            });
        }
    }
});