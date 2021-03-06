Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
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
            'full_name_of_lead': null,
            'phone_number': null,
            'email': null,
            'lead_conversion': null,
            'customer_representative': null,
            'status': null,
            'financial_status': null,
            'call_duration': 0.00,
            'total_time_transferring_leads': 0.00,
            'notes': null,
        },

        newMasterBoard: {
            'date_started': null,
            'due_date': null,
            'type_of_plan': null,
            'type_of_crm': null,
            'type_of_voip': null,
            'client_name': null,
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
            'call_forwarding_details': null,
            'email_form_forwarding': null
        },

        // for normal search inventory
        inventory_client_name: '',

        // for normal search masterboard
        masterboard_client_name: '',

        //search and load based on the current month
        search_month: '',


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
        this.setCurrentMonth();
        this.setCurrentDate();
        this.searchMonth();
    },
    methods: {
        setCurrentMonth: function () {
            let currentMonth = moment(new Date()).format("MM");
            this.search_month = currentMonth;
        },
        setCurrentDate: function () {
            let currentDate = moment(new Date()).format("YYYY-MM-DD");
            this.newInventory.date_lead_received = currentDate;
            this.newInventory.transferred_date = currentDate;
            this.newMasterBoard.date_started = currentDate;
        },
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
        searchMonth: function () {
            this.loading = true;
            this.$http.get(`/api/v1/callme-financial-report/?date__month=${this.search_month}`)
                .then((response) => {
                    this.loading = false;
                    this.financial = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        resetInventory: function () {
            Object.keys(this.newInventory).forEach(key => {
                this.newInventory[key] = ""
            })
            this.newInventory.call_duration = 0.00;
            this.newInventory.total_time_transferring_leads = 0.00;
            this.setCurrentDate();
        },
        resetBoard: function () {
            Object.keys(this.newMasterBoard).forEach(key => {
                this.newMasterBoard[key] = ""
            })
        },
        getInventory: function () {
            this.loading = true;
            axios.get(`/api/v1/callme-inventory/`)
                .then((response) => {
                    this.loading = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        getBoard: function () {
            this.loading = true;
            axios.get(`/api/v1/callme-masterboard/`)
                .then((response) => {
                    this.loading = false;
                    this.masterboard = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        getFinancial: function () {
            this.loading = true;
            axios.get(`/api/v1/callme-financial-report/`)
                .then((response) => {
                    this.loading = false;
                    this.financial = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        viewInventory: function (id) {
            this.viewing = true;
            axios.get(`/api/v1/callme-inventory/${id}/`)
                .then((response) => {
                    this.viewing = false;
                    this.currentInventories = response.data;
                })
                .catch((err) => {
                    this.viewing = false;
                    console.log(err.response.data);
                })
        },
        viewBoard: function (id) {
            this.viewing = true;
            axios.get(`/api/v1/callme-masterboard/${id}/`)
                .then((response) => {
                    this.viewing = false;
                    this.currentBoards = response.data;
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
        addInventory: function () {
            this.saving = true;
            axios.post('/api/v1/callme-inventory/', this.newInventory)
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
                    swal({
                        title: "GPG System",
                        text: "Please check the summaries of your request. If the problem persist, please contact the admin.",
                        icon: "error",
                        buttons: "Ok",
                    })
                    this.saving = true;
                    this.errored = true;
                    this.errorInventory = err.body;
                    console.log(err.response.data);
                })
        },
        addBoard: function () {
            this.saving = true;
            axios.post('/api/v1/callme-masterboard/', this.newMasterBoard)
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
                    this.saving = true;
                    this.errored = true;
                    swal({
                        title: "GPG System",
                        text: "Please check the summaries of your request. If the problem persist, please contact the admin.",
                        icon: "error",
                        buttons: "Ok",
                    })
                    this.errorBoard = err.body;
                    console.log(err.response.data);
                })
        },
        updateInventory: function () {
            this.saving = true;
            axios.put(`/api/v1/callme-inventory/${this.currentInventories.id}/`, this.currentInventories)
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
                    console.log(err.response.data);
                })
        },
        updateBoard: function () {
            this.saving = true;
            axios.put(`/api/v1/callme-masterboard/${this.currentBoards.id}/`, this.currentBoards)
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
                    console.log(err.response.data);
                })
        },
        normalSearchInventory: function () {
            this.searching = true;
            axios.get(`/api/v1/callme-inventory/?client_full_name=${this.inventory_client_name}`)
                .then((response) => {
                    this.searching = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        normalSearchBoard: function () {
            this.searching = true;
            axios.get(`/api/v1/callme-masterboard/?client_name=${this.masterboard_client_name}`)
                .then((response) => {
                    this.searching = false;
                    this.masterboard = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        advancedSearchBoard: function () {
            this.searching = true;
            axios.get(`/api/v1/callme-masterboard/?date_started=${this.search_date_started}&type_of_crm=${this.search_crm}&type_of_voip=${this.search_voip}&client_name=${this.search_client_name_board}&url_buyer=${this.search_url_buyer}&url_seller${this.search_url_buyer}=&url_property_management=${this.search_url_property_management}&general_calls=${this.search_general_calls}&voicemail=${this.search_voicemail}`)
                .then((response) => {
                    this.searching = false;
                    this.masterboard = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        advancedSearchInventory: function () {
            this.searching = true;
            axios.get(`/api/v1/callme-inventory/?client_full_name=${this.search_client_name_inventory}&type_of_form=${this.search_type_of_form}&financial_status=${this.search_financial_status}&customer_representative=${this.search_csr}&status=${this.search_status}&lead_transferred_by=${this.search_transferred_by}`)
                .then((response) => {
                    this.searching = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
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
        generateExcelFile: function () {
            let uri = 'data:application/vnd.ms-excel;base64,';

            let context = {
                worksheet: 'Worksheet1',
                header: this.htmlConverter(this.generateExcelHeader()),
                table: this.generateRows()
            }
            let htmlXML = this.generateXMLNS();
            let formattedTemplate = this.formatTemplate(htmlXML, context);
            let a = document.createElement('A');
            a.href = uri + this.base64(formattedTemplate);
            a.download = 'call-me-inventory-report-' + Date.now() + '.xlsx';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        },
        htmlConverter: function (data) {
            temporaryContainer = document.createElement('div');
            temporaryContainer.appendChild(data);

            return temporaryContainer.innerHTML
        },
        generateRows: function () {
            let inventory = this.inventory;
            let tableRows = '';

            for (let i = 0; i < inventory.length; i++) {
                tableRows += this.htmlConverter(
                    this.generateData(inventory[i])
                );
            }

            return tableRows

        },
        generateData: function (inventory) {
            let tr = document.createElement('tr');

            let transferredDate = document.createElement('td');
            let dateLeadReceived = document.createElement('td');
            let typeOfForm = document.createElement('td');
            let clientFullName = document.createElement('td');
            let fullNameOfLead = document.createElement('td');
            let phoneNumber = document.createElement('td');
            let email = document.createElement('td');
            let customerRepresentative = document.createElement('td');
            let status = document.createElement('td');
            let leadTransferredBy = document.createElement('td');
            let financialStatus = document.createElement('td');
            let callDuration = document.createElement('td');
            let totalTimeTransferringLeads = document.createElement('td');
            let totalMins = document.createElement('td');
            let notes = document.createElement('td');
            let leadConversion = document.createElement('td');

            transferredDate.textContent = inventory['transferred_date'];
            dateLeadReceived.textContent = inventory['date_lead_received'];
            typeOfForm.textContent = inventory['type_of_form'];
            clientFullName.textContent = inventory['client_full_name'];
            fullNameOfLead.textContent = inventory['full_name_of_lead'];
            phoneNumber.textContent = inventory['phone_number'];
            email.textContent = inventory['email'];
            customerRepresentative.textContent = inventory['customer_representative'];
            status.textContent = inventory['status'];
            leadTransferredBy.textContent = inventory['lead_transferred_by'];
            financialStatus.textContent = inventory['financial_status'];
            callDuration.textContent = inventory['call_duration'];
            totalTimeTransferringLeads.textContent = inventory['total_time_transferring_leads'];
            totalMins.textContent = inventory['total_mins'];
            notes.textContent = inventory['notes'];
            leadConversion.textContent = inventory['lead_conversion'];

            tr.appendChild(transferredDate);
            tr.appendChild(dateLeadReceived);
            tr.appendChild(typeOfForm);
            tr.appendChild(clientFullName);
            tr.appendChild(fullNameOfLead);
            tr.appendChild(phoneNumber);
            tr.appendChild(email);
            tr.appendChild(customerRepresentative);
            tr.appendChild(status);
            tr.appendChild(leadTransferredBy);
            tr.appendChild(financialStatus);
            tr.appendChild(callDuration);
            tr.appendChild(totalTimeTransferringLeads);
            tr.appendChild(totalMins);
            tr.appendChild(notes);
            tr.appendChild(leadConversion);

            return tr
        },
        generateExcelHeader: function (inventory) {
            let tr = document.createElement('tr');

            let transferredDate = document.createElement('th');
            let dateLeadReceived = document.createElement('th');
            let typeOfForm = document.createElement('th');
            let clientFullName = document.createElement('th');
            let fullNameOfLead = document.createElement('th');
            let phoneNumber = document.createElement('th');
            let email = document.createElement('th');
            let customerRepresentative = document.createElement('th');
            let status = document.createElement('th');
            let leadTransferredBy = document.createElement('th');
            let financialStatus = document.createElement('th');
            let callDuration = document.createElement('th');
            let totalTimeTransferringLeads = document.createElement('th');
            let totalMins = document.createElement('th');
            let notes = document.createElement('th');
            let leadConversion = document.createElement('th');

            transferredDate.textContent = 'Transferred Date';
            dateLeadReceived.textContent = 'Date Lead Received';
            typeOfForm.textContent = 'Type of Form';
            clientFullName.textContent = 'Client name';
            fullNameOfLead.textContent = 'Full name of the Lead';
            phoneNumber.textContent = 'Phone Number';
            email.textContent = 'Email';
            customerRepresentative.textContent = 'Customer Representative';
            status.textContent = 'Status';
            leadTransferredBy.textContent = 'Lead Transferred By';
            financialStatus.textContent = 'Financial Status';
            callDuration.textContent = 'Call Duration';
            totalTimeTransferringLeads.textContent = 'Total Time Transferring Leads';
            totalMins.textContent = 'Total Mins';
            notes.textContent = 'Notes';
            leadConversion.textContent = 'Lead Conversion';

            tr.appendChild(transferredDate);
            tr.appendChild(dateLeadReceived);
            tr.appendChild(typeOfForm);
            tr.appendChild(clientFullName);
            tr.appendChild(fullNameOfLead);
            tr.appendChild(phoneNumber);
            tr.appendChild(email);
            tr.appendChild(customerRepresentative);
            tr.appendChild(status);
            tr.appendChild(leadTransferredBy);
            tr.appendChild(financialStatus);
            tr.appendChild(callDuration);
            tr.appendChild(totalTimeTransferringLeads);
            tr.appendChild(totalMins);
            tr.appendChild(notes);
            tr.appendChild(leadConversion);

            return tr
        },
        generateXMLNS: function () {
            let htmlOpenTag = '<html xmlns:o="urn:schemas-microsoft.com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">';
            let htmlHead = '<head><!-- [if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>{worksheet}</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--><meta http-equiv="content-type" content="text/plain; charset=UTF-8"></head>';
            let htmlBody = '<body><table>{header}{table}</table></body>';
            let htmlCloseTag = '</html>';

            return htmlOpenTag + htmlHead + htmlBody + htmlCloseTag;
        },
        base64: function (template) {
            return window.btoa(unescape(encodeURIComponent(template)))
        },
        formatTemplate: function (template, context) {
            return template.replace(/{(\w+)}/g, function (m, p) { return context[p] })
        },
        generatePDF: function (id, buttonNumber) {
            this.loadButton(buttonNumber);

            let link = document.createElement('a');
            link.href = `/land-master/${id}/inventory-report.pdf`;
            link.download = 'inventory-Report-' + Date.now();
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        },
        loadButton: function (buttonNumber) {
            Vue.set(this.buttonsLoading, buttonNumber, 1);

            let self = this;

            setTimeout(function () {
                Vue.set(self.buttonsLoading, buttonNumber, 0);
            }, 8000);
        }
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
                let start = (this.currentFinancialPage - 1) * this.pageFinancialSize;
                let end = this.currentFinancialPage * this.pageFinancialSize;
                if (index >= start && index < end) return true;
            });
        },
        sortedMinutes: function () {
            return this.financial.sort((a, b) => {
                let modifier = 1;
                if (this.currentSortDir === 'desc') modifier = -1;
                if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
                if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
                return 0;
            }).filter((row, index) => {
                let start = (this.currentFinancialPage - 1) * this.pageFinancialSize;
                let end = this.currentFinancialPage * this.pageFinancialSize;
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
        },
        totalMinutesUsed: function () {
            return this.financial.reduce(function (sum, financial) {
                return sum + parseFloat(financial.total_minutes_used);
            }, 0);
        },
        totalExcessMinutes: function () {
            return this.financial.reduce(function (sum, financial) {
                return sum + parseFloat(financial.excess_minutes);
            }, 0);
        }
    }
});
