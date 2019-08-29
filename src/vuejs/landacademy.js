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
        fetching: false,
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
            'researcher_name': null,
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
            this.fetching = true;
            axios.get(`/api/v1/staffs/`)
                .then((response) => {
                    this.staffs = response.data;
                    this.fetching = false;
                })
                .catch((err) => {
                    this.fetching = false;
                    console.log(err.response.data);
                })
        },
        getClients: function () {
            this.fetching = true;
            axios.get(`/api/v1/client/`)
                .then((response) => {
                    this.clients = response.data;
                    this.fetching = false;
                })
                .catch((err) => {
                    this.fetching = false;
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
        },
        generateLandAcademyExcelFile: function () {
            let uri = 'data:application/vnd.ms-excel;base64,';

            let context = {
                worksheet: 'Worksheet1',
                header: this.htmlConverter(this.generateLandAcademyExcelHeader()),
                table: this.generateLandAcademyRows()
            }
            let htmlXML = this.generateXMLNS();
            let formattedTemplate = this.formatTemplate(htmlXML, context);
            let a = document.createElement('A');
            a.href = uri + this.base64(formattedTemplate);
            a.download = 'Land-Academy-Inventory-Report-' + Date.now() + '.xlsx';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        },
        htmlConverter: function (data) {
            temporaryContainer = document.createElement('div');
            temporaryContainer.appendChild(data);

            return temporaryContainer.innerHTML
        },
        generateLandAcademyRows: function () {
            let landacademy = this.landacademy;
            let tableRows = '';

            for (let i = 0; i < landacademy.length; i++) {
                tableRows += this.htmlConverter(
                    this.generateLandAcademyData(landacademy[i])
                );
            }

            return tableRows
        },
        generateLandAcademyData: function (landacademy) {
            let tr = document.createElement('tr');

            let dateRequested = document.createElement('td');
            let dateCompleted = document.createElement('td');
            let datePaymentMade = document.createElement('td');
            let orderName = document.createElement('td');
            let clientLARequestor = document.createElement('td');
            let completeOrder = document.createElement('td');
            let statusOfOrder = document.createElement('td');
            let paymentStatus = document.createElement('td');
            let invoice = document.createElement('td');
            let totalItemsCharge = document.createElement('td');
            let totalPayPalFee = document.createElement('td');
            let totalCharge = document.createElement('td');
            let totalItemsRequested = document.createElement('td');
            let notes = document.createElement('td');

            dateRequested.textContent = landacademy['date_requested'];
            dateCompleted.textContent = landacademy['date_completed'];
            datePaymentMade.textContent = landacademy['date_payment_made'];
            orderName.textContent = landacademy['order_name'];
            clientLARequestor.textContent = landacademy['client_la_requestor'];
            completeOrder.textContent = landacademy['complete_order'];
            statusOfOrder.textContent = landacademy['status_of_order'];
            paymentStatus.textContent = landacademy['payment_status'];
            invoice.textContent = landacademy['invoice'];
            totalItemsCharge.textContent = landacademy['total_items_charge'];
            totalPayPalFee.textContent = landacademy['total_pp_fee'];
            totalCharge.textContent = landacademy['total_charge'];
            totalItemsRequested.textContent = landacademy['total_items_requested'];
            notes.textContent = landacademy['notes'];

            tr.appendChild(dateRequested);
            tr.appendChild(dateCompleted);
            tr.appendChild(datePaymentMade);
            tr.appendChild(orderName);
            tr.appendChild(clientLARequestor);
            tr.appendChild(completeOrder);
            tr.appendChild(statusOfOrder);
            tr.appendChild(paymentStatus);
            tr.appendChild(invoice);
            tr.appendChild(totalItemsCharge);
            tr.appendChild(totalPayPalFee);
            tr.appendChild(totalCharge);
            tr.appendChild(totalItemsRequested);
            tr.appendChild(notes);

            return tr
        },
        generateLandAcademyExcelHeader: function (landacademy) {
            let tr = document.createElement('tr');

            let dateRequested = document.createElement('th');
            let dateCompleted = document.createElement('th');
            let datePaymentMade = document.createElement('th');
            let orderName = document.createElement('th');
            let clientLARequestor = document.createElement('th');
            let completeOrder = document.createElement('th');
            let statusOfOrder = document.createElement('th');
            let paymentStatus = document.createElement('th');
            let invoice = document.createElement('th');
            let totalItemsCharge = document.createElement('th');
            let totalPayPalFee = document.createElement('th');
            let totalCharge = document.createElement('th');
            let totalItemsRequested = document.createElement('th');
            let notes = document.createElement('th');

            dateRequested.textContent = 'Date Requested';
            dateCompleted.textContent = 'Date Completed';
            datePaymentMade.textContent = 'Date Payment Made';
            orderName.textContent = 'Order Name';
            clientLARequestor.textContent = 'Client LA Requestor';
            completeOrder.textContent = 'Complete Order';
            statusOfOrder.textContent = 'Status of Order';
            paymentStatus.textContent = 'Payment Status';
            invoice.textContent = 'Invoice';
            totalItemsCharge.textContent = 'Total Items Charge';
            totalPayPalFee.textContent = 'Total Paypal Fee';
            totalCharge.textContent = 'Total Charge';
            totalItemsRequested.textContent = 'Total Items Requested';
            notes.textContent = 'Notes';

            tr.appendChild(dateRequested);
            tr.appendChild(dateCompleted);
            tr.appendChild(datePaymentMade);
            tr.appendChild(orderName);
            tr.appendChild(clientLARequestor);
            tr.appendChild(completeOrder);
            tr.appendChild(statusOfOrder);
            tr.appendChild(paymentStatus);
            tr.appendChild(invoice);
            tr.appendChild(totalItemsCharge);
            tr.appendChild(totalPayPalFee);
            tr.appendChild(totalCharge);
            tr.appendChild(totalItemsRequested);
            tr.appendChild(notes);

            return tr
        },
        generateO2OExcelFile: function () {
            let uri = 'data:application/vnd.ms-excel;base64,';

            let context = {
                worksheet: 'Worksheet1',
                header: this.htmlConverter(this.generateO2OExcelHeader()),
                table: this.generateO2ORows()
            }
            let htmlXML = this.generateXMLNS();
            let formattedTemplate = this.formatTemplate(htmlXML, context);
            let a = document.createElement('A');
            a.href = uri + this.base64(formattedTemplate);
            a.download = 'O2O-Smart-Pricing-Report-' + Date.now() + '.xlsx';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        },
        htmlConverter: function (data) {
            temporaryContainer = document.createElement('div');
            temporaryContainer.appendChild(data);

            return temporaryContainer.innerHTML
        },
        generateO2ORows: function () {
            let smartpricing = this.smartpricing;
            let tableRows = '';

            for (let i = 0; i < smartpricing.length; i++) {
                tableRows += this.htmlConverter(
                    this.generateO2OData(smartpricing[i])
                );
            }

            return tableRows
        },
        generateO2OData: function (smartpricing) {
            let tr = document.createElement('tr');

            let dateRequested = document.createElement('td');
            let dateResearch = document.createElement('td');
            let dateEncoded = document.createElement('td');
            let situsAddress = document.createElement('td');
            let trulia = document.createElement('td');
            let zillow = document.createElement('td');
            let redfin = document.createElement('td');
            let realfor = document.createElement('td');
            let realtytrac = document.createElement('td');
            let orderName = document.createElement('td');
            let requestorFullName = document.createElement('td');
            let researcherName = document.createElement('td');
            let qualityCheckStatus = document.createElement('td');
            let qualitySpecialist = document.createElement('td');
            let notesFromResearcher = document.createElement('td');
            let notesFromQa = document.createElement('td');

            dateRequested.textContent = smartpricing['date_requested'];
            dateResearch.textContent = smartpricing['date_research'];
            dateEncoded.textContent = smartpricing['date_encoded'];
            situsAddress.textContent = smartpricing['situs_address'];
            trulia.textContent = smartpricing['trulia'];
            zillow.textContent = smartpricing['zillow'];
            redfin.textContent = smartpricing['redfin'];
            realfor.textContent = smartpricing['realfor'];
            realtytrac.textContent = smartpricing['realtytrac'];
            orderName.textContent = smartpricing['order_name'];
            requestorFullName.textContent = smartpricing['requestor_full_name'];
            researcherName.textContent = smartpricing['researcher_name'];
            qualityCheckStatus.textContent = smartpricing['quality_check_status'];
            qualitySpecialist.textContent = smartpricing['quality_specialist'];
            notesFromResearcher.textContent = smartpricing['notes_from_researcher'];
            notesFromQa.textContent = smartpricing['notes_from_qa'];

            tr.appendChild(dateRequested);
            tr.appendChild(dateResearch);
            tr.appendChild(dateEncoded);
            tr.appendChild(situsAddress);
            tr.appendChild(trulia);
            tr.appendChild(zillow);
            tr.appendChild(redfin);
            tr.appendChild(realfor);
            tr.appendChild(realtytrac);
            tr.appendChild(orderName);
            tr.appendChild(requestorFullName);
            tr.appendChild(researcherName);
            tr.appendChild(qualityCheckStatus);
            tr.appendChild(qualitySpecialist);
            tr.appendChild(notesFromResearcher);
            tr.appendChild(notesFromQa);

            return tr
        },
        generateO2OExcelHeader: function (smartpricing) {
            let tr = document.createElement('tr');

            let dateRequested = document.createElement('th');
            let dateResearch = document.createElement('th');
            let dateEncoded = document.createElement('th');
            let situsAddress = document.createElement('th');
            let trulia = document.createElement('th');
            let zillow = document.createElement('th');
            let redfin = document.createElement('th');
            let realfor = document.createElement('th');
            let realtytrac = document.createElement('th');
            let orderName = document.createElement('th');
            let requestorFullName = document.createElement('th');
            let researcherName = document.createElement('th');
            let qualityCheckStatus = document.createElement('th');
            let qualitySpecialist = document.createElement('th');
            let notesFromResearcher = document.createElement('th');
            let notesFromQa = document.createElement('th');

            dateRequested.textContent = 'Date Requested';
            dateResearch.textContent = 'Date Research';
            dateEncoded.textContent = 'Date Encoded';
            situsAddress.textContent = 'Situs Address';
            trulia.textContent = 'Trulia';
            zillow.textContent = 'Zillow';
            redfin.textContent = 'Redfin';
            realfor.textContent = 'Realfor';
            realtytrac.textContent = 'RealtyTrac';
            orderName.textContent = 'Order Name';
            requestorFullName.textContent = 'Requestor Full Name';
            researcherName.textContent = 'Researcher Name';
            qualityCheckStatus.textContent = 'Quality Check Status';
            qualitySpecialist.textContent = 'Quality Specialist';
            notesFromResearcher.textContent = 'Notes From Researcher';
            notesFromQa.textContent = 'Notes From QA';

            tr.appendChild(dateRequested);
            tr.appendChild(dateResearch);
            tr.appendChild(dateEncoded);
            tr.appendChild(situsAddress);
            tr.appendChild(trulia);
            tr.appendChild(zillow);
            tr.appendChild(redfin);
            tr.appendChild(realfor);
            tr.appendChild(realtytrac);
            tr.appendChild(orderName);
            tr.appendChild(requestorFullName);
            tr.appendChild(researcherName);
            tr.appendChild(qualityCheckStatus);
            tr.appendChild(qualitySpecialist);
            tr.appendChild(notesFromResearcher);
            tr.appendChild(notesFromQa);

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
            return template.replace(/{(\w+)}/g, function (m, p) {
                return context[p]
            })
        },
        generatePDF: function (id, buttonNumber) {
            this.loadButton(buttonNumber);

            let link = document.createElement('a');
            link.href = `/land-academy/${id}/inventory-report.pdf`;
            link.download = 'landacademy-inventory-Report-' + Date.now();
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
