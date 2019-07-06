Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-callme',
    delimiters: ['[[', ']]'],
    data: {
        inventory: [],
        masterboard: [],
        financial: [],
        staffs: [],
        clients: [],
        loading: false,
        viewing: false,
        saving: false,
        searching: false,
        errored: false,
        reverse: false,
        message: null,
        errorInventory: [],
        errorBoard: [],
        currentInventories: [],
        currentBoards: [],
        currentSort: '',
        currentSortDir: 'desc',
        newInventory: {
            'transferred_date': '',
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
            'call_duration': 0.00,
            'total_time_transferring_leads': 0.00,
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
            'notes': null,
            'gs_integration': null,
            'client_folder': null,
            'email': null,
            'phone': null,
            'phone_login': null,
            'crm_login': null,
        },

        // for normal search inventory
        inventory_client_name: '',

        // for normal search masterboard
        masterboard_client_name: '',


        // for advanced search inventory
        search_client_name_inventory: '',
        search_client_company_inventory: '',
        search_csr: '',
        search_status: '',
        search_financial_status: '',
        search_type_of_form: '',
        search_transferred_by: '',

        // for advanced search masterboard
        search_plan: '',
        search_crm: '',
        search_voip: '',
        search_client_name_board: '',
        search_company_name_board: '',
        search_date_started: '',
        search_url_buyer: '',
        search_url_seller: '',
        search_url_property_management: '',
        search_general_calls: '',
        search_voicemail: '',        

        // for pagination
        currentInventoryPage: 1,
        currentMasterBoardPage: 1,
        currentFinancialPage: 1,
        pageInventorySize: RECORDS_PER_PAGE,
        pageMasterBoardSize: RECORDS_PER_PAGE,
        pageFinancialSize: RECORDS_PER_PAGE,
        startInventoryPage: 1,
        startMasterBoardPage: 1,
        endInventoryPage: null,
        endMasterBoardPage: null,
        endFinancialPage: null,
        maxInventoryPages: RECORDS_PER_PAGE,
        maxMasterBoardPages: RECORDS_PER_PAGE,
        paginatedInventoryRecords: [],
        paginatedMasterBoardRecords: [],
    },
    mounted: function () {
        this.getStaffs();
        this.getClients();
        this.getInventory();
        this.getFinancial();
        this.getBoard();
    },
    methods: {
        nextBoardPage: function () {
            if ((this.currentMasterBoardPage * this.pageMasterBoardSize) < this.masterboard.length) this.currentMasterBoardPage++;
        },
        nextFinancialPage: function () {
            if ((this.currentFinancialPage * this.pageFinancialSize) < this.financial.length) this.currentFinancialPage++;
        },
        prevBoardPage: function () {
            if (this.currentMasterBoardPage > 1) this.currentMasterBoardPage--;
        },
        prevFinancialPage: function () {
            if (this.currentFinancialPage > 1) this.currentFinancialPage--;
        },
        sort: function (s) {
            //if s == current sort, reverse
            if (s === this.currentSort) {
                this.currentSortDir = this.currentSortDir === 'asc' ? 'desc' : 'asc';
            }
            this.currentSort = s;
        },
        duration($event) {
            // console.log($event.keyCode); //keyCodes value
            let keyCode = ($event.keyCode ? $event.keyCode : $event.which);

            // only allow number and one dot
            if ((keyCode < 48 || keyCode > 57) && (keyCode !== 46 || this.price.indexOf('.') != -1)) { // 46 is dot
                $event.preventDefault();
            }

            // restrict to 2 decimal places
            if (this.price != null && this.price.indexOf(".") > -1 && (this.price.split('.')[1].length > 1)) {
                $event.preventDefault();
            }
        },
        // This can also prevent copy + paste invalid character
        filterInput(e) {
            e.target.value = e.target.value.replace(/[^0-9]+/g, '');
        },
        resetInventory: function () {
            Object.keys(this.newInventory).forEach(key => {
                this.newInventory[key] = ""
            })
            this.newInventory.call_duration = 0.00;
            this.newInventory.total_time_transferring_leads = 0.00;
        },
        resetBoard: function () {
            Object.keys(this.newMasterBoard).forEach(key => {
                this.newMasterBoard[key] = ""
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
        getFinancial: function () {
            this.loading = true;
            this.$http.get(`/api/v1/callme-financial-report/`)
                .then((response) => {
                    this.loading = false;
                    this.financial = response.data;
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
                    this.resetInventory();
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
                    this.errorInventory = err.body;
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
                    this.resetBoard();
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
                    this.errorBoard = err.body;
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
        normalSearchInventory: function () {
            this.searching = true;
            this.$http.get(`/api/v1/callme-inventory/?client_full_name=${this.inventory_client_name}`)
                .then((response) => {
                    this.searching = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err);
                })
        },
        normalSearchBoard: function () {
            this.searching = true;
            this.$http.get(`/api/v1/callme-masterboard/?client_name=${this.masterboard_client_name}`)
                .then((response) => {
                    this.searching = false;
                    this.masterboard = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err);
                })
        },
        advancedSearchBoard: function () {
            this.searching = true;
            this.$http.get(`/api/v1/callme-masterboard/?date_started=${this.search_date_started}&type_of_crm=${this.search_crm}&type_of_voip=${this.search_voip}&client_name=${this.search_client_name_board}&company_name=${this.search_company_name_board}&url_buyer=${this.search_url_buyer}&url_seller${this.search_url_buyer}=&url_property_management=${this.search_url_property_management}&general_calls=${this.search_general_calls}&voicemail=${this.search_voicemail}`)
                .then((response) => {
                    this.searching = false;
                    this.masterboard = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err);
                })
        },
        advancedSearchInventory: function () {
            this.searching = true;
            this.$http.get(`/api/v1/callme-inventory/?client_full_name=${this.search_client_name_inventory}&client_company_name=${this.search_client_company_inventory}&type_of_form=${this.search_type_of_form}&financial_status=${this.search_financial_status}&customer_representative=${this.search_csr}&status=${this.search_status}&lead_transferred_by=${this.search_transferred_by}`)
                .then((response) => {
                    this.searching = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err);
                })
        },
        getInventoryPaginatedRecords: function () {
            const startInventoryIndex = this.startInventoryIndex;
            this.paginatedInventoryRecords = this.inventory.slice().splice(startInventoryIndex, this.pageInventorySize);
        },
        getMasterBoardPaginatedRecords: function () {
            const startMasterBoardIndex = this.startMasterBoardIndex;
            this.paginatedMasterBoardRecords = this.masterboard.slice().splice(startMasterBoardIndex, this.pageMasterBoardSize);
        },
        goToInventoryPage: function (page) {
            if (page < 1) {
                return this.currentInventoryPage = 1;
            }
            if (page > this.totalInventoryPages) {
                return this.currentInventoryPage = this.totalInventoryPages;
            }
            this.currentInventoryPage = page;
        },
        goToMasterBoardPage: function (page) {
            if (page < 1) {
                return this.currentMasterBoardPage = 1;
            }
            if (page > this.totalMasterBoardPages) {
                return this.currentMasterBoardPage = this.totalMasterBoardPages;
            }
            this.currentMasterBoardPage = page;
        },
        goToFinancialPage: function (page) {
            if (page < 1) {
                return this.currentFinancialPage = 1;
            }
            if (page > this.totalFinancialPages) {
                return this.currentFinancialPage = this.totalFinancialPages;
            }
            this.currentFinancialPage = page;
        },
        setInventoryPageGroup: function () {
            if (this.totalInventoryPages <= this.maxInventoryPages) {
                this.startInventoryPage = 1;
                this.endInventoryPage = Math.min(this.totalInventoryPages, this.maxInventoryPages);
            } else {
                let maxPagesBeforeCurrentPage = Math.floor(this.maxInventoryPages / 2);
                let maxPagesAfterCurrentPage = Math.ceil(this.maxInventoryPages / 2) - 1;
                if (this.currentInventoryPage <= maxPagesBeforeCurrentPage) {
                    // current page near the start
                    this.startInventoryPage = 1;
                    this.endInventoryPage = this.maxInventoryPages;
                } else if (thiscurrentInventoryPage + maxPagesAfterCurrentPage >= this.totalInventoryPages) {
                    // current page near the end
                    this.startInventoryPage = this.totalInventoryPages - this.maxInventoryPages + 1;
                    this.endInventoryPage = this.totalInventoryPages;
                } else {
                    // current page somewhere in the middle
                    this.startInventoryPage = this.currentInventoryPage - maxPagesBeforeCurrentPage;
                    this.endInventoryPage = this.currentInventoryPage + maxPagesAfterCurrentPage;
                }
            }
        },
        setMasterBoardPageGroup: function () {
            if (this.totalMasterBoardPages <= this.maxMasterBoardPages) {
                this.startMasterBoardPage = 1;
                this.endMasterBoardPage = Math.min(this.totalMasterBoardPages, this.maxMasterBoardPages);
            } else {
                let maxPagesBeforeCurrentPage = Math.floor(this.maxMasterBoardPages / 2);
                let maxPagesAfterCurrentPage = Math.ceil(this.maxMasterBoardPages / 2) - 1;
                if (this.currentMasterBoardPage <= maxPagesBeforeCurrentPage) {
                    // current page near the start
                    this.startMasterBoardPage = 1;
                    this.endMasterBoardPage = this.maxMasterBoardPages;
                } else if (thiscurrentMasterBoardPage + maxPagesAfterCurrentPage >= this.totalMasterBoardPages) {
                    // current page near the end
                    this.startMasterBoardPage = this.totalMasterBoardPages - this.maxMasterBoardPages + 1;
                    this.endMasterBoardPage = this.totalMasterBoardPages;
                } else {
                    // current page somewhere in the middle
                    this.startMasterBoardPage = this.currentMasterBoardPage - maxPagesBeforeCurrentPage;
                    this.endMasterBoardPage = this.currentMasterBoardPage + maxPagesAfterCurrentPage;
                }
            }
        },
    },
    watch: {
        masterboard: function (newMasterBoardRecords, oldMasterBoardRecords) {
            this.setMasterBoardPageGroup();
            this.getMasterBoardPaginatedRecords();
        },
        inventory: function (newInventoryRecords, oldInventoryRecords) {
            this.setInventoryPageGroup();
            this.getInventoryPaginatedRecords();
        },
        currentInventoryPage: function (newCurrentInventoryPage, oldCurrentInventoryPage) {
            this.setInventoryPageGroup();
            this.getInventoryPaginatedRecords();
        },
        currentMasterBoardPage: function (newCurrentMasterBoardPage, oldCurrentMasterBoardPage) {
            this.setMasterBoardPageGroup();
            this.getMasterBoardPaginatedRecords();
        },
    },
    computed: {
        totalMasterBoardItems: function () {
            return this.masterboard.length;
        },
        totalInventoryItems: function () {
            return this.inventory.length;
        },
        totalFinancialItems: function () {
            return this.inventory.length;
        },
        totalMasterBoardPages: function () {
            return Math.ceil(this.totalMasterBoardItems / this.pageMasterBoardSize);
        },
        totalInventoryPages: function () {
            return Math.ceil(this.totalInventoryItems / this.pageInventorySize);
        },
        totalFinancialPages: function () {
            return Math.ceil(this.totalFinancialItems / this.pageFinancialSize);
        },
        startMasterBoardIndex: function () {
            return (this.currentMasterBoardPage - 1) * this.pageMasterBoardSize;
        },
        startInventoryIndex: function () {
            return (this.currentInventoryPage - 1) * this.pageInventorySize;
        },
        endMasterBoardIndex: function () {
            return Math.min(this.startMasterBoardIndex + this.pageMasterBoardSize - 1, this.totalMasterBoardItems - 1);
        },
        endInventoryIndex: function () {
            return Math.min(this.startInventoryIndex + this.pageInventorySize - 1, this.totalInventoryItems - 1);
        },
        pagesMasterBoard: function () {
            let pagesMasterBoard = [];
            for (let i = this.startMasterBoardPage; i <= this.endMasterBoardPage; i++) pagesMasterBoard.push(i);
            return pagesMasterBoard;
        },
        pagesInventory: function () {
            let pagesInventory = [];
            for (let i = this.startInventoryPage; i <= this.endInventoryPage; i++) pagesInventory.push(i);
            return pagesInventory;
        },
        sortedMasterBoards: function () {
            return this.masterboard.sort((a, b) => {
                let modifier = 1;
                if (this.currentSortDir === 'desc') modifier = -1;
                if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
                if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
                return 0;
            }).filter((row, index) => {
                let start = (this.currentMasterBoardPage - 1) * this.pageMasterBoardSize;
                let end = this.currentMasterBoardPage * this.pageMasterBoardSize;
                if (index >= start && index < end) return true;
            });
        },
        sortedInventories: function () {
            return this.inventory.sort((a, b) => {
                let modifier = 1;
                if (this.currentSortDir === 'desc') modifier = -1;
                if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
                if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
                return 0;
            }).filter((row, index) => {
                let start = (this.currentInventoryPage - 1) * this.pageInventorySize;
                let end = this.currentInventoryPage * this.pageInventorySize;
                if (index >= start && index < end) return true;
            });
        },
        sortedFinancial: function () {
            return this.financial.sort((a, b) => {
                let modifier = 1;
                if (this.currentSortDir === 'desc') modifier = -1;
                if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
                if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
                return 0;
            }).filter((row, index) => {
                let start = (this.currentInventoryPage - 1) * this.pageInventorySize;
                let end = this.currentInventoryPage * this.pageInventorySize;
                if (index >= start && index < end) return true;
            });
        },
        totalTypePlan: function () {
            return this.financial.reduce(function (sum, financial) {
                return sum + parseFloat(financial.type_of_plan);
            }, 0);
        },
        totalPaymentMade: function () {
            return this.financial.reduce(function (sum, financial) {
                return sum + parseFloat(financial.payment_made);
            }, 0);
        }
    }
});
