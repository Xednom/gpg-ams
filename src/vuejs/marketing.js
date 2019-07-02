Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-marketing',
    delimiters: ['[[', ']]'],
    data: {
        inventory: [],
        staffs: [],
        clients: [],
        loading: false,
        viewing: false,
        saving: false,
        searching: false,
        message: null,
        currentInventories: [],
        newInventory: {
            'date_requested': null,
            'date_completed': null,
            'type_of_marketing_sites': null,
            'indicate_others': null,
            'client_full_name': null,
            'client_company_name': null,
            'apn': null,
            'title_of_the_post': null,
            'description': null,
            'price': null,
            'location': null,
            'url_link': null,
            'marketing_associate': null,
            'duration': null,
            'post_for_approval': null,
            'status': null,
            'additional_notes': null,
            'notes_from_the_client': null,
        },

        // for normal search
        search_client_full_name: '',

        // for advance search
        advance_date_requested: '',
        advance_date_completed: '',
        advance_type_of_marketing_sites: '',
        advance_client_full_name: '',
        advance_client_company_name: '',
        advance_apn: '',
        advance_status: '',
        advance_post_for_approval: '',

        
        // for pagination
        currentPage: 1,
        pageSize: RECORDS_PER_PAGE,
        startPage: 1,
        endPage: null,
        maxPages: RECORDS_PER_PAGE,
        paginatedRecords: [],
    },
    mounted: function () {
        this.getInventory();
        this.getStaffs();
        this.getClients();
    },
    methods: {
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
        reset: function () {
            Object.keys(this.newInventory).forEach(key => {
                this.newInventory[key] = ""
            })
        },
        getInventory: function () {
            this.loading = true;
            this.$http.get(`/api/v1/marketing-sites/`)
                .then((response) => {
                    this.loading = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        viewInventory: function (id) {
            this.viewing = true;
            this.$http.get(`/api/v1/marketing-sites/${id}/`)
                .then((response) => {
                    this.viewing = false;
                    this.currentInventories = response.data;
                })
                .catch((err) => {
                    this.viewing = false;
                    console.log(err);
                })
        },
        getStaffs: function () {
            this.loading = true;
            this.$http.get(`/api/v1/staffs/`)
                .then((response) => {
                    this.staffs = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getClients: function () {
            this.loading = true;
            this.$http.get(`/api/v1/clients/`)
                .then((response) => {
                    this.clients = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addInventory: function () {
            this.saving = true;
            this.$http.post('/api/v1/marketing-sites/', this.newInventory)
                .then((response) => {
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: "Inventory informations has been added successfully! You can add another one.",
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
                    console.log(err);
                })
        },
        updateInventory: function () {
            this.saving = true;
            this.$http.put(`/api/v1/marketing-sites/${this.currentInventories.id}/`, this.currentInventories)
                .then((response) => {
                    this.saving = false;
                    this.currentInventories = response.data;
                    swal({
                        title: "GPG system",
                        text: "Successfully updated the informations!",
                        icon: "success",
                        button: false,
                        timer: 1500
                    })
                    $("#editModal").modal('hide')
                    this.getInventory();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        normalSearchInventory: function () {
            this.searching = true;
            this.$http.get(`/api/v1/marketing-sites/?client_full_name=${this.search_client_full_name}`)
                .then((response) => {
                    this.searching = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err);
                })
        },
        advanceSearchInventory: function () {
            this.searching = true;
            this.$http.get(`/api/v1/marketing-sites/?date_requested=${this.advance_date_requested}&date_completed=${this.advance_date_completed}&type_of_marketing_sites=${this.advance_type_of_marketing_sites}&client_full_name=${this.advance_client_full_name}&client_company_name=${this.advance_client_company_name}&apn=${this.advance_apn}&status=${this.advance_status}&post_for_approval=${this.advance_post_for_approval}`)
                .then((response) => {
                    this.searching = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err);
                })
        },
        getPaginatedRecords: function () {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.inventory.slice().splice(startIndex, this.pageSize);
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
        inventory: function (newInventoryRecords, oldInventoryRecords) {
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
            return this.inventory.length;
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
