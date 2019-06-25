Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-callme',
    delimiters: ['[[', ']]'],
    data: {
        inventory: [],
        masterboard: [],
        staffs: [],
        clients: [],
        loading: false,
        viewing: false,
        saving: false,
        message: null,
        currentInventories: [],
        currentBoards: [],
        newInventory: {
            'transferred_date': null,
            'date_lead_received': null,
            'type_of_form': null,
            'client_full_name': null,
            'client_company_name': null,
            'full_name_of_lead': null,
            'phone_number': null,
            'email': null,
            'customer_representative': null,
            'status': null,
            'financial_status': null,
            'call_duration': null,
            'total_time_transferring_leads': null,
            'total_mins': null,
            'notes': null,
        },

        newMasterBoard: {
            'date_started': null,
            'type_of_plan': null,
            'type_of_crm': null,
            'type_of_voip': null,
            'client_name': null,
            'company_name': null,
            'url_buyer': null,
            'url_seller': null,
            'url_property_management': null,
            'voicemail': null,
            'general_calls': null,
        },

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
        this.getInventory();
        this.getBoard();
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
            this.$http.get(`/api/v1/callme-inventory/`)
                .then((response) => {
                    this.loading = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getBoard: function () {
            this.loading = true;
            this.$http.get(`/api/v1/callme-masterboard/`)
                .then((response) => {
                    this.loading = false;
                    this.masterboard = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        viewInventory: function (id) {
            this.viewing = true;
            this.$http.get(`/api/v1/callme-inventory/${id}/`)
                .then((response) => {
                    this.viewing = false;
                    this.currentInventories = response.data;
                })
                .catch((err) => {
                    this.viewing = false;
                    console.log(err);
                })
        },
        viewBoard: function (id) {
            this.viewing = true;
            this.$http.get(`/api/v1/callme-masterboard/${id}/`)
                .then((response) => {
                    this.viewing = false;
                    this.currentBoards = response.data;
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
            this.$http.get(`/api/v1/clients-callme/`)
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
            this.$http.post('/api/v1/callme-inventory/', this.newInventory)
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
        addBoard: function () {
            this.saving = true;
            this.$http.post('/api/v1/callme-masterboard/', this.newMasterBoard)
                .then((response) => {
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: "Master Board informations has been added successfully! You can add another one.",
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
            this.$http.put(`/api/v1/callme-inventory/${this.currentInventories.id}/`, this.currentInventories)
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
        updateBoard: function () {
            this.saving = true;
            this.$http.put(`/api/v1/callme-masterboard/${this.currentBoards.id}/`, this.currentBoards)
                .then((response) => {
                    this.saving = false;
                    this.currentBoards = response.data;
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
