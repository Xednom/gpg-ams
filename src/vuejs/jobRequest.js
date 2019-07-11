Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#gpg-job-request',
  delimiters: ['[[',']]'],
  data: {
    jobRequests: [],
    statusOfTheJobRequests: [],
    projectManagers: [],
    virtualAssistants: [],
    jobRequestTitles: [],
    companyNames: [],
    companyAssignedTo: [],
    loading: false,
    saving: false,
    currentJobRequest: {},
    message: null,
    result2: null,
    newJobRequest: {
      'category': null,
      'date_requested': null,
      'due_date': null,
      'month': null,
      'requestors_name': null,
      'company_name': null,
      'job_request_number': null,
      'job_request_title': null,
      'job_request_instruction': null,
      'additional_comments_or_feedbacks': null,
      'assigned_project_managers': null,
      'project_status': null,
      'url_training_videos': null,
      'assigned_va': null,
      'time_in': null,
      'time_out': null,
      'manager_notes': null,
      'client_notes': null,
      'va_notes': null,
      'company_billable_to': null,
      'company_asigned_to': null,
      'authorized_minutes_hours_allocation': null,
    },
    search_term: '',
    // for pagination
    currentPage: 1,
    pageSize: RECORDS_PER_PAGE,
    startPage: 1,
    endPage: null,
    maxPages: RECORDS_PER_PAGE,
    paginatedRecords: [],
  },
  mounted: function() {
    this.getJobRequests();
    //this.getStatusOfJobRequest();
    this.setDefaultDates();
    this.getProjectManagers();
    this.getJobRequestTitles();
    // this.setDefaultTimeInAndOut();
    this.getVAs();
  },
  methods: {
    setDefaultDates: function () {
      let currentDate = moment(new Date()).format("YYYY-MM-DD");
      this.newJobRequest.date_requested = currentDate;
      this.newJobRequest.due_date = currentDate;
    },
    setDefaultTimeInAndOut: function () {
      let currentDate = moment(new Date()).format("YYYY-MM-DD hh:mm A");
      this.currentJobRequest.time_in = currentDate;
      this.currentJobRequest.time_out = currentDate;
    },
    reset: function() {
      Object.keys(this.newJobRequest).forEach(key => {
        this.newJobRequest[key] = ""
      })
    },
    getJobRequests: function() {
      api_url = `/api/v1/jobrequest/?search=${this.search_term}`
      this.loading = false;
      this.$http.get(api_url)
          .then((response) => {
            this.jobRequests = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getJobRequest: function(id) {
      this.loading = true;
      this.$http.get(`/api/v1/jobrequest/${id}/`)
          .then((response) => {
            this.currentJobRequest = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getJobRequestTitles: function () {
      this.loading = true;
      this.$http.get(`/api/v1/job-request-title/`)
        .then((response) => {
          this.jobRequestTitles = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
    getStatusOfJobRequest: function() {
      this.loading = true;
      this.$http.get(`/api/v1/status-of-the-job-request/`)
          .then((response) => {
            this.statusOfTheJobRequests = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getProjectManagers: function() {
      this.loading = true;
      this.$http.get(`/api/v1/pms/`)
          .then((response) => {
            this.projectManagers = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getVAs: function () {
      this.loading = true;
      this.$http.get(`/api/v1/vas/`)
        .then((response) => {
          this.virtualAssistants = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
    getCompanyNames: function () {
      this.loading = true;
      this.$http.get(`/api/v1/virtual-assistant/`)
        .then((response) => {
          this.virtualAssistants = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
    },
    addJobRequest: function() {
      this.saving = true;
      this.$http.post('/api/v1/jobrequest/', this.newJobRequest)
          .then((response) => {
            this.saving = false;
            this.getJobRequests();
            swal({
              title: "GPG System",
              text: "Job Request has been added successfully",
              icon: "success",
              buttons: false,
              timer: 1500
            })
            this.reset();
          })
          .catch((err) => {
            this.loading = false;
            swal({
              title: "GPG System",
              text: "Please try again later, and if the error persist. Please contact the admin.",
              // text: JSON.stringify(err.body), this is a sample stack trace for furture reference
              icon: "error",
              buttons: "Ok",
            });
            console.log(err);
          })
    },
    updateJobRequest: function() {
      this.loading = true;
      this.$http.put(`/api/v1/jobrequest/${this.currentJobRequest.id}/`, this.currentJobRequest)
          .then((response) => {
            this.loading = false;
            this.currentJobRequest = response.data;
            swal({
              title: "GPG system",
              text: "Successfully updated the data!",
              icon: "success",
              button: false,
              timer: 1500
            });
            $("#editModal").modal('hide')
            this.getJobRequests();
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    deleteJobRequest: function(id) {
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
          this.$http.delete(`/api/v1/jobrequest/${id}/`)
              .then((response) => {
                this.loading = false;
                this.getJobRequests();
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
        this.paginatedRecords = this.jobRequests.slice().splice(startIndex, this.pageSize);
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
      jobRequests: function (newjobRequestsRecords, oldjobRequestsRecords) {
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
        return this.jobRequests.length;
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
});
