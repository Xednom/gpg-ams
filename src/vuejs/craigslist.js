Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
new Vue({
    el: '#gpg-craigslist',
    delimiters: ['[[', ']]'],
    data: {
        craigslist: [],
        clients: [],
        staffs: [],
        loading: false,
        searching: false,
        viewing: false,
        errored: false,
        saving: false,
        currentCraigList: {},
        message: null,
        newCraigList: {
            'client_name_company_name': null,
            'cl_admin_support': null,
            'date': null,
            'posted_ads': null,
            'flagged_ads': null,
            'sticked_ads': null,
            'stick_rates': null,
            'notes': null,
        },
        search_date: '',
        search_client: '',
        search_admin_support: '',
        search_name: '',

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
        this.getCraigsList();
        this.getClients();
        this.getStaffs();
    },
    methods: {
        reset: function () {
            Object.keys(this.newCraigList).forEach(key => {
                this.newCraigList[key] = ""
            })
        },
        sort: function (s) {
            //if s == current sort, reverse
            if (s === this.currentSort) {
                this.currentSortDir = this.currentSortDir === 'asc' ? 'desc' : 'asc';
            }
            this.currentSort = s;
        },
        setCurrentMonth() {
            let currentMonth = moment(new Date()).format("MM");
            this.search_month = currentMonth;
        },
        getCraigsList() {
            this.loading = true;
            axios.get(`/api/v1/craigslist/`)
                .then((response) => {
                    this.loading = false;
                    this.craigslist = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        viewCraigslist(id) {
            this.viewing = true;
            axios.get(`/api/v1/craigslist/${id}`)
                .then((response) => {
                    this.viewing = false;
                    this.currentCraigList = response.data;
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
        searchAll() {
            this.searching = true;
            axios.get(`/api/v1/craigslist/?date=${this.search_date}&client_name=${this.search_client}&cl_admin_support=${this.search_admin_support}`)
                .then((response) => {
                    this.searching = false;
                    this.craigslist = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        searchName() {
            this.searching = true;
            axios.get(`/api/v1/craigslist/?date=&client_name=${this.search_name}&cl_admin_support=${this.search_name}`)
                .then((response) => {
                    this.searching = false;
                    this.craigslist = response.data;
                })
                .catch((err) => {
                    this.searching = false;
                    console.log(err.response.data);
                })
        },
        addInventory: function () {
            this.saving = true;
            axios.post('/api/v1/craigslist/', this.newCraigList)
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
            axios.put(`/api/v1/craigslist/${this.currentCraigList.id}/`, this.currentCraigList)
                .then((response) => {
                    this.saving = false;
                    this.currentCraigList = response.data;
                    swal({
                        title: "GPG system",
                        text: "Successfully updated the information(s)!",
                        icon: "success",
                        button: false,
                        timer: 1500
                    })
                    $("#editModal").modal('hide')
                    this.getCraigsList();
                })
                .catch((err) => {
                    this.saving = false;
                    console.log(err.response.data);
                })
        },
        getPaginatedRecords() {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.craigslist.slice().splice(startIndex, this.pageSize);
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
        generatePDF: function (id, buttonNumber) {
            this.loadButton(buttonNumber);

            let link = document.createElement('a');
            link.href = `/payroll/${id}/payroll-report.pdf`;
            link.download = 'payroll-Report-' + Date.now();
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
        craigslist: function (newCraigsListRecords, oldCraigsListRecords) {
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
            return this.craigslist.length;
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
        sortedCraigslist() {
            return this.craigslist.sort((a, b) => {
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
