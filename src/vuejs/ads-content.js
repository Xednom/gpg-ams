Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
new Vue({
    el: "#gpg-ads",
    delimiters: ['[[', ']]'],
    data: {
        ads: [],
        clients: [],
        staffs: [],
        loading: false,
        fetching: false,
        viewing: false,
        searching: false,
        saving: false,
        errored: false,
        currentAds: [],
        currentSort: [],
        currentSortDir: 'desc',
        newAds: {
            'due_date': null,
            'date_completed': null,
            'client': null,
            'apn_or_items_needs_ad_content': "",
            'client_recommendation': "",
            'content_instruction': "",
            'content_finished': "",
            'final_title': "",
            'modification': "",
            'content_status': "",
            'ads_writer':null,
            'additional_notes': "",
        },

        // pagination
        currentPage: 1,
        pageSize: RECORDS_PER_PAGE,
        startPage: 1,
        endPage: null,
        maxPages: RECORDS_PER_PAGE,
        paginatedRecords: []
    },
    mounted() {
        this.getAds();
    },
    methods: {
        nextPage() {
            if ((this.currentPage * this.pageSize) < this.ads.length) this.currentPage++;
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
        resetAdsFields() {
            Object.keys(this.newAds).forEach(key => {
                this.newAds[key] = ""
            })
        },
        getAds() {
            this.loading = true;
            axios.get(`/api/v1/ads/`)
                .then((response) => {
                    this.loading = false;
                    this.ads = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getStaffs() {
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
        getClients() {
            this.fetching = true;
            axios.get(`/api/v1/clients/`)
                .then((response) => {
                    this.clients = response.data;
                    this.fetching = false;
                })
                .catch((err) => {
                    this.fetching = false;
                    console.log(err.response.data);
                })
        },
        viewAds(id) {
            this.viewing = true;
            axios.get(`/api/v1/ads/${id}/`)
                .then((response) => {
                    this.getClients();
                    this.getStaffs();
                    this.viewing = false;
                    this.currentAds = response.data;
                })
                .catch((err) => {
                    this.viewing = false;
                    console.log(err.response.data);
                })
        },
        addAds() {
            this.saving = true;
            axios.post('/api/v1/ads/', this.newAds)
                .then((response) => {
                    this.saving = false;
                    this.resetAdsFields();
                    swal({
                        title: "GPG System",
                        text: "Ad(s) has been added successfully!",
                        icon: "success",
                        buttons: false,
                        timer: 3000
                    })
                })
                .catch((error) => {
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: "Please check the summaries of your request. If the problem persist, please contact the admin.",
                        icon: "error",
                        buttons: "Ok",
                    })
                    console.log(error.response.data);
                })
        },
        updateAds() {
            this.saving = true;
            axios.put(`/api/v1/ads/${this.currentAds.id}/`, this.currentAds)
                .then((response) => {
                    this.saving = false;
                    this.currentAds = response.data;
                    swal({
                        title: "GPG system",
                        text: "Successfully updated the data!",
                        icon: "success",
                        button: false,
                        timer: 1500
                    });
                    $("#editModal").modal('hide')
                    this.getAds();
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
        getPaginatedRecords() {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.ads.slice().splice(startIndex, this.pageSize);
        },
        goToPage(page) {
            if (page < 1) {
                return this.currentPage = 1;
            }
            if (page > this.totalPages) {
                return this.currentPage = this.totalPages;
            }
            this.currentPage = page;
        },
        setPageGroup() {
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
        sortedAds() {
            return this.ads.sort((a, b) => {
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