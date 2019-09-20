Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
new Vue({
    el: "#gpg-client-lead",
    delimiters: ['[[', ']]'],
    data: {
        leads: [],
        clients: [],
        staffs: [],
        loading: false,
        fetching: false,
        viewing: false,
        searching: false,
        saving: false,
        errored: false,
        currentLeads: [],
        currentSort: [],
        currentSortDir: 'desc',

        // pagination
        currentPage: 1,
        pageSize: RECORDS_PER_PAGE,
        startPage: 1,
        endPage: null,
        maxPages: RECORDS_PER_PAGE,
        paginatedRecords: []
    },
    mounted() {
        this.getLeads();
        this.getClients();
        this.getStaffs();
    },
    methods: {
        nextPage() {
            if ((this.currentPage * this.pageSize) < this.leads.length) this.currentPage++;
        },
        prevPage() {
            if (this.currentPage > 1) this.currentPage--;
        },
        prevPage() {
            if (this.currentPage > 1) this.currentPage--;
        },
        sort(s) {
            //if s == current sort, reverse
            if (s === this.currentSort) {
                this.currentSortDir = this.currentSortDir === 'asc' ? 'desc' : 'asc';
            }
            this.currentSort = s;
        },
        getLeads() {
            this.loading = true;
            axios.get(`/api/v1/lead-source/`)
                .then((response) => {
                    this.loading = false;
                    this.leads = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
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
        viewLeads: function (id) {
            this.viewing = true;
            axios.get(`/api/v1/lead-source/${id}/`)
                .then((response) => {
                    this.viewing = false;
                    this.currentLeads = response.data;
                })
                .catch((err) => {
                    this.viewing = false;
                    console.log(err.response.data);
                })
        },
        updateLeads() {
            this.saving = true;
            axios.put(`/api/v1/lead-source/${this.currentLeads.id}/`, this.currentLeads)
                .then((response) => {
                    this.saving = false;
                    this.currentLeads = response.data;
                    swal({
                        title: "GPG system",
                        text: "Successfully updated the data!",
                        icon: "success",
                        button: false,
                        timer: 1500
                    });
                    $("#editModal").modal('hide')
                    this.getLeads();
                })
                .catch((err) => {
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: JSON.stringify(err.body),
                        icon: "error",
                        buttons: false,
                        timer: 3000,
                    });
                    console.log(err.response.data);
                })
        },
        getPaginatedRecords: function () {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.leads.slice().splice(startIndex, this.pageSize);
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
                if (this.currentInventoryPage <= maxPagesBeforeCurrentPage) {
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
    },
    computed: {
        sortedLeads: function () {
            return this.leads.sort((a, b) => {
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
    }
})