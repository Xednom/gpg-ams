Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-reminders',
    delimiters: ['[[', ']]'],
    data: {
        reminders: [],
        loading: false,
        message: null,
        newReminder: {
            'description': null,
            'manager_under': null,
            'due_date': null,
            'status': null,
            'notes_from_company': null,
            'notes_from_manager': null,
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
        this.getreminders();
    },
    methods: {
        resetFields: function () {
            Object.keys(this.newReminder).forEach(key => {
                this.newReminder[key] = ""
            })
        },
        setCurrentMonth: function () {
            let currentMonth = moment(new Date()).format("MM");
            this.search_month = currentMonth;
        },
        searchAll: function () {
            this.searchMonthReminder();
        },
        searchMonthReminder: function () {
            this.loading = true;
            this.$http.get(`/api/v1/reminders/?date__month=${this.search_month}`)
                .then((response) => {
                    this.loading = false;
                    this.reminders = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getreminders: function () {
            let api_url = '/api/v1/reminders/';
            this.loading = true;
            this.$http.get(api_url)
                .then((response) => {
                    this.reminders = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addReminder: function () {
            this.saving = true;
            this.$http.post('/api/v1/reminders/', this.newReminder)
                .then((response) => {
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: "Reminder has been added successfully! You can add another one.",
                        icon: "success",
                        buttons: false,
                        timer: 3000
                    })
                    this.resetFields();
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
                    this.errorduediligence = err.body;
                    console.log(err);
                })
        },
        deleteReminder: function (id) {
            swal({
                    title: "Are you sure?",
                    text: "Once deleted, you will not be able to recover this data!",
                    icon: "warning",
                    buttons: true,
                    dangerMode: true,
                })
                .then((willDelete) => {
                    if (willDelete) {
                        this.loading = true;
                        this.$http.delete(`/api/v1/reminders/${id}`)
                            .then((response) => {
                                this.loading = false;
                                this.getreminders();
                            })
                            .catch((err) => {
                                this.loading = false;
                                console.log(err);
                            })
                        swal("Poof! Your data file has been deleted!", {
                            icon: "success",
                            button: false,
                            timer: 1500
                        });
                    } else {
                        swal({
                            text: "Your data is safe.",
                            icon: "success",
                            button: false,
                            timer: 1500
                        });
                    }
                });
        },
        getPaginatedRecords: function () {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.reminders.slice().splice(startIndex, this.pageSize);
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
        reminders: function (newReminderRecords, oldReminderRecords) {
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
            return this.reminders.length;
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
