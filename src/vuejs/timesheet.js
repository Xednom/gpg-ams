Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
new Vue({
    el: '#gpg-timesheet',
    delimiters: ['[[', ']]'],
    data: {
        timesheets: [],
        cashouts: [],
        clients: [],
        paymentmade: [],
        errortimesheet: [],
        loading: false,
        viewing: false,
        searching: false,
        saving: false,
        errored: false,
        currentTimeSheet: {},
        message: null,
        newTimeSheet: {
            'company_tagging': null,
            'shift_date': null,
            'month_to_date': null,
            'clients_full_name': null,
            'title_job_request': null,
            'channel_job_requested': null,
            'job_request_description': null,
            'time_in': null,
            'time_out': null,
            'duration': null,
            'total_items': null,
            'additional_comments': null,
            'assigned_va': null,
            'assigned_pm': null,
            'hourly_rate_peso': null,
            'hourly_rate_usd': null,
            'total_charge_peso': null,
            'total_charge_usd': null,
            'paypal_charge': null,
            'total_charge_with_paypal': null,
            'total_amount_due': null,
            'status': null,
            'admin_approval': null
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
        this.searchMonthVaTimeSheet();
        this.searchMonthClientTimeSheet();
        this.loadClient();
        this.searchMonthCashOut();
        this.getCashOut();
    },
    methods: {
        setCurrentMonth: function () {
            let currentMonth = moment(new Date()).format("MM");
            this.search_month = currentMonth;
        },
        getTimeSheet: function () {
            this.loading = true;
            axios.get(`/api/v1/timesheet/`)
                .then((response) => {
                    this.loading = false;
                    this.timesheets = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        getCashOut: function () {
            this.loading = true;
            axios.get(`/api/v1/cashout/`)
                .then((response) => {
                    this.loading = false;
                    this.cashouts = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        searchMonthVaTimeSheet() {
            this.searching = true;
            axios.get(`/api/v1/timesheet/?shift_date__month=${this.search_month}`)
                .then((response) => {
                    this.searching = false;
                    this.timesheets = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        searchMonthCashOut: function () {
            this.searching = true;
            axios.get(`/api/v1/cashout/?cash_date_release__month=${this.search_month}`)
                .then((response) => {
                    this.searching = false;
                    this.cashouts = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        searchAll: function () {
            this.searchMonthClientTimeSheet();
            this.searchMonthVaTimeSheet();
            this.searchMonthPaymentMade();
            this.searchMonthCashOut();
        },
        searchMonthClientTimeSheet: function () {
            this.searching = true;
            axios.get(`/api/v1/timesheet/?shift_date__month=${this.search_month}`)
                .then((response) => {
                    this.searching = false;
                    this.timesheets = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        viewTimeSheet(id) {
            this.viewing = true;
            axios.get(`/api/v1/timesheet/${id}`)
                .then((response) => {
                    this.viewing = false;
                    this.currentTimeSheet = response.data;
                })
                .catch((err) => {
                    this.viewing = false;
                    this.errored = true;
                    this.errortimesheet = err.body;
                    console.log(err.response.data);
                })
        },
        updateTimeSheet() {
            this.saving = true;
            axios.put(`/api/v1/timesheet/${this.currentTimeSheet.id}/`, this.currentTimeSheet)
                .then((response) => {
                    this.saving = false;
                    this.currentTimeSheet = response.data;
                    swal({
                        title: "GPG system",
                        text: "Successfully updated the informations!",
                        icon: "success",
                        button: false,
                        timer: 1500
                    })
                    $("#viewModal").modal('hide')
                    this.getTimeSheet();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        loadClient() {
            this.loading = true;
            axios.get(`/api/v1/clients`)
                .then((response) => {
                    this.loading = false;
                    this.clients = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    this.errored = true;
                    console.log(err.response.data);
                })
        },
        searchMonthPaymentMade() {
            this.searching = true;
            axios.get(`/api/v1/paymentmade/?date__month=${this.search_month}`)
                .then((response) => {
                    this.searching = false;
                    this.paymentmade = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        getPaymentMade: function () {
            this.loading = true;
            axios.get(`/api/v1/paymentmade`)
                .then((response) => {
                    this.loading = false;
                    this.paymentmade = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
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
            a.download = 'timesheet-report-' + Date.now() + '.xlsx';
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
            let timesheets = this.timesheets;
            let tableRows = '';

            for (let i = 0; i < timesheets.length; i++) {
                tableRows += this.htmlConverter(
                    this.generateData(timesheets[i])
                );
            }

            return tableRows

        },
        generateData: function (timesheets) {
            let tr = document.createElement('tr');

            let companyTagging = document.createElement('td');
            let shiftDate = document.createElement('td');
            let monthToDate = document.createElement('td');
            let clientsFullName = document.createElement('td');
            let titleJobRequest = document.createElement('td');
            let channelJobRequested = document.createElement('td');
            let jobRequestDescription = document.createElement('td');
            let timeIn = document.createElement('td');
            let timeOut = document.createElement('td');
            let duration = document.createElement('td');
            let totalItems = document.createElement('td');
            let additionalComments = document.createElement('td');
            let assignedVa = document.createElement('td');
            let assignedPm = document.createElement('td');
            let hourlyRateUsd = document.createElement('td');
            let totalChargeUsd = document.createElement('td');
            let totalAmountDue = document.createElement('td');
            let bonusGivenToCompany = document.createElement('td');
            let othersDollars = document.createElement('td');

            companyTagging.textContent = timesheets['company_tagging'];
            shiftDate.textContent = timesheets['shift_date'];
            monthToDate.textContent = timesheets['month_to_date'];
            clientsFullName.textContent = timesheets['clients_full_name'];
            titleJobRequest.textContent = timesheets['title_job_request'];
            channelJobRequested.textContent = timesheets['channel_job_requested'];
            jobRequestDescription.textContent = timesheets['job_request_description'];
            timeIn.textContent = timesheets['time_in'];
            timeOut.textContent = timesheets['time_out'];
            duration.textContent = timesheets['duration'];
            totalItems.textContent = timesheets['total_items'];
            additionalComments.textContent = timesheets['additional_comments'];
            assignedVa.textContent = timesheets['assigned_va'];
            assignedPm.textContent = timesheets['assigned_pm'];
            hourlyRateUsd.textContent = timesheets['hourly_rate_usd'];
            totalChargeUsd.textContent = timesheets['total_charge_usd'];
            totalAmountDue.textContent = timesheets['total_amount_due'];
            bonusGivenToCompany.textContent = timesheets['bonus_given_to_company'];
            othersDollars.textContent = timesheets['others_dollars'];

            tr.appendChild(companyTagging);
            tr.appendChild(shiftDate);
            tr.appendChild(monthToDate);
            tr.appendChild(clientsFullName);
            tr.appendChild(titleJobRequest);
            tr.appendChild(channelJobRequested);
            tr.appendChild(jobRequestDescription);
            tr.appendChild(timeIn);
            tr.appendChild(timeOut);
            tr.appendChild(duration);
            tr.appendChild(totalItems);
            tr.appendChild(additionalComments);
            tr.appendChild(assignedVa);
            tr.appendChild(assignedPm);
            tr.appendChild(hourlyRateUsd);
            tr.appendChild(totalChargeUsd);
            tr.appendChild(totalAmountDue);
            tr.appendChild(bonusGivenToCompany);
            tr.appendChild(othersDollars);

            return tr
        },
        generateExcelHeader: function (timesheets) {
            let tr = document.createElement('tr');

            let companyTagging = document.createElement('th');
            let shiftDate = document.createElement('th');
            let monthToDate = document.createElement('th');
            let clientsFullName = document.createElement('th');
            let titleJobRequest = document.createElement('th');
            let channelJobRequested = document.createElement('th');
            let jobRequestDescription = document.createElement('th');
            let timeIn = document.createElement('th');
            let timeOut = document.createElement('th');
            let duration = document.createElement('th');
            let totalItems = document.createElement('th');
            let additionalComments = document.createElement('th');
            let assignedVa = document.createElement('th');
            let assignedPm = document.createElement('th');
            let hourlyRateUsd = document.createElement('th');
            let totalChargeUsd = document.createElement('th');
            let totalAmountDue = document.createElement('th');
            let bonusGivenToCompany = document.createElement('th');
            let othersDollars = document.createElement('th');

            companyTagging.textContent = 'Company tagging';
            shiftDate.textContent = 'Shift to Date';
            monthToDate.textContent = 'Month to Date';
            clientsFullName.textContent = "Client's Full name";
            titleJobRequest.textContent = 'Title Job Request';
            channelJobRequested.textContent = "Channel job requested";
            jobRequestDescription.textContent = 'job Request Description';
            timeIn.textContent = 'Time In';
            timeOut.textContent = 'Time Out';
            duration.textContent = 'Duration';
            totalItems.textContent = 'Total items';
            additionalComments.textContent = 'Additional Comments';
            assignedVa.textContent = 'Assigned Va';
            assignedPm.textContent = 'Assigned Project Manager';
            hourlyRateUsd.textContent = 'Hourly Rate';
            totalChargeUsd.textContent = 'Total Charge';
            totalAmountDue.textContent = 'Total Amount Due';
            bonusGivenToCompany.textContent = 'Bonus Given to Company';
            othersDollars.textContent = 'Others';

            tr.appendChild(companyTagging);
            tr.appendChild(shiftDate);
            tr.appendChild(monthToDate);
            tr.appendChild(clientsFullName);
            tr.appendChild(titleJobRequest);
            tr.appendChild(channelJobRequested);
            tr.appendChild(jobRequestDescription);
            tr.appendChild(timeIn);
            tr.appendChild(timeOut);
            tr.appendChild(duration);
            tr.appendChild(totalItems);
            tr.appendChild(additionalComments);
            tr.appendChild(assignedVa);
            tr.appendChild(assignedPm);
            tr.appendChild(hourlyRateUsd);
            tr.appendChild(totalChargeUsd);
            tr.appendChild(totalAmountDue);
            tr.appendChild(bonusGivenToCompany);
            tr.appendChild(othersDollars);

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
            link.href = `/land-master/${id}/timesheets-report.pdf`;
            link.download = 'marketing-sites-timesheets-Report-' + Date.now();
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
        totalCashOut: function () {
            return this.cashouts.reduce(function (sum, cashouts) {
                return sum + parseFloat(cashouts.amount);
            }, 0);
        },
        totalCreditsLeft: function () {
            let sum = this.totalpaymentmade - this.totalTimeSheet;
            return sum.toFixed(2);
        },
        totalSalaryVa() {
            return this.timesheets.reduce(function (sum, timesheets) {
                return sum + parseFloat(timesheets.total_charge_peso)
            }, 0)
        },
        totalWorkHrs() {
            return this.timesheets.reduce(function (sum, timesheets) {
                return sum + parseFloat(timesheets.duration)
            }, 0)
        },
        totalDueStaffs() {
            let sum = this.totalSalaryVa - this.totalCashOut;
            return sum.toFixed(2);
        }
    }
});
