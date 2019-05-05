Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-due-diligence-tracker',
    delimiters: ['[[', ']]'],
    data: {
        loading: false,
        saving: false,
        duediligencestracking: [],
        currentDueDiligencesTracking: [],

        // for pagination
        currentPage: 1,
        pageSize: RECORDS_PER_PAGE,
        startPage: 1,
        endPage: null,
        maxPages: RECORDS_PER_PAGE,
        paginatedRecords: [],
    },
    mounted: function () {
        this.getDueDiligenceCleared();
    },
    methods: {
        getDueDiligenceCleared: function () {
            this.loading = true;
            this.$http.get(`/api/v1/due-diligence-tracker/`)
                .then((response) => {
                    this.duediligencestracking = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        updateDueDiligenceCleared: function () {
            this.loading = true;
            this.$http.put(`/api/v1/due-diligence-tracker/${this.currentDueDiligencesTracking.id}/`, this.currentDueDiligencesTracking)
                .then((response) => {
                    this.loading = false;
                    this.currentDueDiligencesTracking = response.data;
                    swal({
                        title: "GPG system",
                        text: "Successfully updated the data!",
                        icon: "success",
                        button: false,
                        timer: 2000
                    });
                    $("#editModal").modal('hide')
                    this.getDueDiligenceCleared();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        viewDueDiligenceCleared: function (id) {
            this.loading = true;
            this.$http.get(`/api/v1/due-diligence-tracker/${id}`)
                .then((response) => {
                    this.loading = false;
                    this.currentDueDiligencesTracking = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getPaginatedRecords: function () {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.duediligencestracking.slice().splice(startIndex, this.pageSize);
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
                } else if (this.currentPage + maxPagesAfterCurrentPage >= this.totalPages) {
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
        duediligencestracking: function (newduediligencestrackingRecords, oldduediligencestrackingRecords) {
            this.setPageGroup();
            this.getPaginatedRecords();
        },
        currentPage: function (newCurrentPage, oldCurrentPage) {
            this.setPageGroup();
            this.getPaginatedRecords()
        },
    },
    computed: {
        totalItems: function () {
            return this.duediligencestracking.length;
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
    },
})