Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
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
        currentSort: '',
        currentSortDir: 'desc',
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
        nextPage: function () {
            if ((this.currentPage * this.pageSize) < this.landacademy.length) this.currentPage++;
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
        reset: function () {
            Object.keys(this.newInventory).forEach(key => {
                this.newInventory[key] = ""
            })
        },
        getInventory: function () {
            this.loading = true;
            axios.get(`/api/v1/marketing-sites/`)
                .then((response) => {
                    this.loading = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        viewInventory: function (id) {
            this.viewing = true;
            axios.get(`/api/v1/marketing-sites/${id}/`)
                .then((response) => {
                    this.viewing = false;
                    this.currentInventories = response.data;
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
            axios.get(`/api/v1/clients/`)
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
            axios.post('/api/v1/marketing-sites/', this.newInventory)
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
                    console.log(err.response.data);
                })
        },
        updateInventory: function () {
            this.saving = true;
            axios.put(`/api/v1/marketing-sites/${this.currentInventories.id}/`, this.currentInventories)
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
        normalSearchInventory: function () {
            this.searching = true;
            axios.get(`/api/v1/marketing-sites/?client_full_name=${this.search_client_full_name}`)
                .then((response) => {
                    this.searching = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        advanceSearchInventory: function () {
            this.searching = true;
            axios.get(`/api/v1/marketing-sites/?date_requested=${this.advance_date_requested}&date_completed=${this.advance_date_completed}&type_of_marketing_sites=${this.advance_type_of_marketing_sites}&client_full_name=${this.advance_client_full_name}&client_company_name=${this.advance_client_company_name}&apn=${this.advance_apn}&status=${this.advance_status}&post_for_approval=${this.advance_post_for_approval}`)
                .then((response) => {
                    this.searching = false;
                    this.inventory = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
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

            let dateRequested = document.createElement('td');
            let dateCompleted = document.createElement('td');
            let typeOfMarketingSites = document.createElement('td');
            let indicateOthers = document.createElement('td');
            let clientFullName = document.createElement('td');
            let clientCompanyName = document.createElement('td');
            let apn = document.createElement('td');
            let titleOfThePost = document.createElement('td');
            let description = document.createElement('td');
            let price = document.createElement('td');
            let location = document.createElement('td');
            let urlLink = document.createElement('td');
            let marketingAssociate = document.createElement('td');
            let duration = document.createElement('td');
            let postForApproval = document.createElement('td');
            let status = document.createElement('td');
            let additionalNotes = document.createElement('td');
            let notesFromTheClient = document.createElement('td');

            dateRequested.textContent = inventory['date_requested'];
            dateCompleted.textContent = inventory['date_completed'];
            typeOfMarketingSites.textContent = inventory['type_of_marketing_sites'];
            indicateOthers.textContent = inventory['indicate_others'];
            clientFullName.textContent = inventory['client_full_name'];
            clientCompanyName.textContent = inventory['client_company_name'];
            apn.textContent = inventory['apn'];
            titleOfThePost.textContent = inventory['title_of_the_post'];
            description.textContent = inventory['description'];
            price.textContent = inventory['price'];
            location.textContent = inventory['location'];
            urlLink.textContent = inventory['url_link'];
            marketingAssociate.textContent = inventory['marketing_associate'];
            duration.textContent = inventory['duration'];
            postForApproval.textContent = inventory['post_for_approval'];
            status.textContent = inventory['status'];
            additionalNotes.textContent = inventory['additional_notes'];
            notesFromTheClient.textContent = inventory['notes_from_the_client'];

            tr.appendChild(dateRequested);
            tr.appendChild(dateCompleted);
            tr.appendChild(typeOfMarketingSites);
            tr.appendChild(indicateOthers);
            tr.appendChild(clientFullName);
            tr.appendChild(clientCompanyName);
            tr.appendChild(apn);
            tr.appendChild(titleOfThePost);
            tr.appendChild(description);
            tr.appendChild(price);
            tr.appendChild(location);
            tr.appendChild(urlLink);
            tr.appendChild(marketingAssociate);
            tr.appendChild(duration);
            tr.appendChild(postForApproval);
            tr.appendChild(status);
            tr.appendChild(additionalNotes);
            tr.appendChild(notesFromTheClient);

            return tr
        },
        generateExcelHeader: function (inventory) {
            let tr = document.createElement('tr');

            let dateRequested = document.createElement('th');
            let dateCompleted = document.createElement('th');
            let typeOfMarketingSites = document.createElement('th');
            let indicateOthers = document.createElement('th');
            let clientFullName = document.createElement('th');
            let clientCompanyName = document.createElement('th');
            let apn = document.createElement('th');
            let titleOfThePost = document.createElement('th');
            let description = document.createElement('th');
            let price = document.createElement('th');
            let location = document.createElement('th');
            let urlLink = document.createElement('th');
            let marketingAssociate = document.createElement('th');
            let duration = document.createElement('th');
            let postForApproval = document.createElement('th');
            let status = document.createElement('th');
            let additionalNotes = document.createElement('th');
            let notesFromTheClient = document.createElement('th');

            dateRequested.textContent = 'Date Requested';
            dateCompleted.textContent = 'Date Completed';
            typeOfMarketingSites.textContent = 'Type of Marketing Sites';
            indicateOthers.textContent = 'Indicate Others';
            clientFullName.textContent = 'Client full name';
            clientCompanyName.textContent = 'Client Company name';
            apn.textContent = 'APN';
            titleOfThePost.textContent = 'Title of the Post';
            description.textContent = 'Description';
            price.textContent = 'Price';
            location.textContent = 'Location';
            urlLink.textContent = 'URL Link';
            marketingAssociate.textContent = 'Marketing Associate';
            duration.textContent = 'Duration';
            postForApproval.textContent = 'Post for Approval';
            status.textContent = 'Status';
            additionalNotes.textContent = 'Additional Notes';
            notesFromTheClient.textContent = 'Notes from the Client';

            tr.appendChild(dateRequested);
            tr.appendChild(dateCompleted);
            tr.appendChild(typeOfMarketingSites);
            tr.appendChild(indicateOthers);
            tr.appendChild(clientFullName);
            tr.appendChild(clientCompanyName);
            tr.appendChild(apn);
            tr.appendChild(titleOfThePost);
            tr.appendChild(description);
            tr.appendChild(price);
            tr.appendChild(location);
            tr.appendChild(urlLink);
            tr.appendChild(marketingAssociate);
            tr.appendChild(duration);
            tr.appendChild(postForApproval);
            tr.appendChild(status);
            tr.appendChild(additionalNotes);
            tr.appendChild(notesFromTheClient);

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
            link.download = 'marketing-sites-inventory-Report-' + Date.now();
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
        sortedMarketing: function () {
            return this.inventory.sort((a, b) => {
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
