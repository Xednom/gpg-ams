Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
new Vue({
  el: '#gpg-job-request',
  delimiters: ['[[',']]'],
  data: {
    jobRequests: [],
    jobRequestsTitle: [],
    timesheets: [],
    clients: [],
    statusOfTheJobRequests: [],
    projectManagers: [],
    virtualAssistants: [],
    jobRequestTitles: [],
    companyNames: [],
    companyAssignedTo: [],
    loading: false,
    viewing: false,
    saving: false,
    currentJobRequest: {},
    currentTimeSheet: {},
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
    currentJobRequestPage: 1,
    currentTimeSheetPage: 1,
    pageJobRequestSize: RECORDS_PER_PAGE,
    pageTimeSheetSize: RECORDS_PER_PAGE,
    startJobRequestPage: 1,
    startTimeSheetPage: 1,
    endJobRequestPage: null,
    endTimeSheetPage: null,
    maxJobRequestPages: RECORDS_PER_PAGE,
    maxTimeSheetPages: RECORDS_PER_PAGE,
    paginatedJobRequestRecords: [],
    paginatedTimeSheetRecords: [],
  },
  mounted: function() {
    this.getJobRequests();
    this.getTimeSheets();
    //this.getStatusOfJobRequest();
    this.setDefaultDates();
    this.getProjectManagers();
    this.getJobRequestTitles();
    // this.setDefaultTimeInAndOut();
    this.getVAs();
    this.getClients();
    this.getJobTitle();
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
        this.setDefaultDates();
      })
    },
    nextJobRequestPage: function () {
      if ((this.currentJobRequestPage * this.pageJobRequestSize) < this.jobRequests.length) this.currentJobRequestPage++;
    },
    prevJobRequestPage: function () {
      if (this.currentJobRequestPage > 1) this.currentJobRequestPage--;
    },
    getJobRequests: function() {
      api_url = `/api/v1/jobrequest/?search=${this.search_term}`
      this.loading = true;
      axios.get(api_url)
          .then((response) => {
            this.jobRequests = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err.response.data);
          })
    },
    getTimeSheets: function (id) {
      this.loading = true;
      axios.get(`/api/v1/job-request-timesheet/`)
        .then((response) => {
          this.timesheets = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err.response.data);
        })
    },
    getJobTitle: function () {
      api_url = `/api/v1/jobrequest/`
      this.loading = true;
      axios.get(api_url)
        .then((response) => {
          this.jobRequestsTitle = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err.response.data);
        })
    },
    getJobRequest: function(id) {
      this.viewing = true;
      axios.get(`/api/v1/jobrequest/${id}/`)
          .then((response) => {
            this.currentJobRequest = response.data;
            this.viewing = false;
          })
          .catch((err) => {
            this.viewing = false;
            console.log(err.response.data);
          })
    },
    getTimeSheet: function (id) {
      this.loading = true;
      axios.get(`/api/v1/job-request-timesheet/${id}/`)
        .then((response) => {
          this.currentTimeSheet = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err.response.data);
        })
    },
    getJobRequestTitles: function () {
      this.loading = true;
      axios.get(`/api/v1/job-request-title/`)
        .then((response) => {
          this.jobRequestTitles = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err.response.data);
        })
    },
    getStatusOfJobRequest: function() {
      this.loading = true;
      axios.get(`/api/v1/status-of-the-job-request/`)
          .then((response) => {
            this.statusOfTheJobRequests = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err.response.data);
          })
    },
    getProjectManagers: function() {
      this.loading = true;
      axios.get(`/api/v1/pms/`)
          .then((response) => {
            this.projectManagers = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err.response.data);
          })
    },
    getVAs: function () {
      this.loading = true;
      axios.get(`/api/v1/vas/`)
        .then((response) => {
          this.virtualAssistants = response.data;
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
    getCompanyNames: function () {
      this.loading = true;
      axios.get(`/api/v1/virtual-assistant/`)
        .then((response) => {
          this.virtualAssistants = response.data;
          this.loading = false;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err.response.data);
        })
    },
    addJobRequest: function() {
      this.saving = true;
      axios.post('/api/v1/jobrequest/', this.newJobRequest)
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
            console.log(err.response.data);
          })
    },
    updateJobRequest: function() {
      this.loading = true;
      this.saving = true
      axios.put(`/api/v1/jobrequest/${this.currentJobRequest.id}/`, this.currentJobRequest)
          .then((response) => {
            this.loading = false;
            this.saving = false;
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
            this.saving = false;
            console.log(err.response.data);
          })
    },
    updateTimeSheet: function () {
      this.loading = true;
      axios.put(`/api/v1/job-request-timesheet/${this.currentTimeSheet.id}/`, this.currentTimeSheet)
        .then((response) => {
          this.loading = false;
          this.currentTimeSheet = response.data;
          swal({
            title: "GPG system",
            text: "Successfully updated the data!",
            icon: "success",
            button: false,
            timer: 1500
          });
          $("#editModal").modal('hide')
          this.getTimeSheets();
        })
        .catch((err) => {
          this.loading = false;
          console.log(err.response.data);
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
          axios.delete(`/api/v1/jobrequest/${id}/`)
              .then((response) => {
                this.loading = false;
                this.getJobRequests();
              })
              .catch((err) => {
                this.loading = false;
                console.log(err.response.data);
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
    getPaginatedJobRequestRecords() {
      const startJobRequestIndex = this.startJobRequestIndex;
      this.paginatedJobRequestRecords = this.jobRequests.slice().splice(startJobRequestIndex, this.pageJobRequestSize);
    },
    getPaginatedTimeSheetRecords() {
      const startTimeSheetIndex = this.startTimeSheetIndex;
      this.paginatedTimeSheetRecords = this.timesheets.slice().splice(startTimeSheetIndex, this.pageTimeSheetSize);
    },
    goToJobRequestPage(page) {
      if (page < 1) {
        return this.currentJobRequestPage = 1;
      }
      if (page > this.totalJobRequestPages) {
        return this.currentJobRequestPage = this.currentJobRequestPage;
      }
      this.currentJobRequestPage = page;
    },
    goToTimeSheetPage(page) {
      if (page < 1) {
        return this.currentTimeSheetPage = 1;
      }
      if (page > this.totalTimeSheetPages) {
        return this.currentTimeSheetPage = this.currentTimeSheetPage;
      }
      this.currentTimeSheetPage = page;
    },
    setPageJobRequestGroup() {
      if (this.totalJobRequestPages <= this.maxJobRequestPages) {
        this.startJobRequestPage = 1;
        this.endJobRequestPage = Math.min(this.totalJobRequestPages, this.maxJobRequestPages);
      } else {
        let maxPagesBeforeCurrentPage = Math.floor(this.maxJobRequestPages / 2);
        let maxPagesAfterCurrentPage = Math.ceil(this.maxJobRequestPages / 2) - 1;
        if (this.currentJobRequestPage <= maxPagesBeforeCurrentPage) {
          // current page near the start
          this.startJobRequestPage = 1;
          this.endJobRequestPage = this.maxJobRequestPages;
        } else if (this.currentJobRequestPage + maxPagesAfterCurrentPage >= this.totalJobRequestPages) {
          // current page near the end
          this.startJobRequestPage = this.totalJobRequestPages - this.maxJobRequestPages + 1;
          this.endJobRequestPage = this.totalJobRequestPages;
        } else {
          // current page somewhere in the middle
          this.startJobRequestPage = this.currentJobRequestPage - maxPagesBeforeCurrentPage;
          this.endJobRequestPage = this.currentJobRequestPage + maxPagesAfterCurrentPage;
        }
      }
    },
    setPageTimeSheetGroup() {
      if (this.totalTimeSheetPages <= this.maxTimeSheetPages) {
        this.startTimeSheetPage = 1;
        this.endTimeSheetPage = Math.min(this.totalTimeSheetPages, this.maxTimeSheetPages);
      } else {
        let maxPagesBeforeCurrentPage = Math.floor(this.maxTimeSheetPages / 2);
        let maxPagesAfterCurrentPage = Math.ceil(this.maxTimeSheetPages / 2) - 1;
        if (this.currentTimeSheetPage <= maxPagesBeforeCurrentPage) {
          // current page near the start
          this.startTimeSheetPage = 1;
          this.endTimeSheetPage = this.maxTimeSheetPages;
        } else if (this.currentTimeSheetPage + maxPagesAfterCurrentPage >= this.totalTimeSheetPages) {
          // current page near the end
          this.startTimeSheetPage = this.totalTimeSheetPages - this.maxTimeSheetPages + 1;
          this.endTimeSheetPage = this.totalTimeSheetPages;
        } else {
          // current page somewhere in the middle
          this.startTimeSheetPage = this.currentTimeSheetPage - maxPagesBeforeCurrentPage;
          this.endTimeSheetPage = this.currentTimeSheetPage + maxPagesAfterCurrentPage;
        }
      }
    }
  },
  watch: {
      jobRequests(newjobRequestsRecords, oldjobRequestsRecords) {
        this.setPageJobRequestGroup();
        this.getPaginatedJobRequestRecords();
      },
      timesheets(newjobRequestsRecords, oldjobRequestsRecords) {
        this.setPageTimeSheetGroup();
        this.getPaginatedTimeSheetRecords();
      },
      currentJobRequestPage(newCurrentPage, oldCurrentPage) {
        this.setPageJobRequestGroup();
        this.getPaginatedJobRequestRecords();
      },
      currentTimeSheetPage(newCurrentPage, oldCurrentPage) {
        this.setPageTimeSheetGroup();
        this.getPaginatedTimeSheetRecords();
      },
    },
    computed: {
      totalJobRequestItems() {
        return this.jobRequests.length;
      },
      totalTimeSheetItems() {
        return this.timesheets.length;
      },
      totalJobRequestPages() {
        return Math.ceil(this.totalJobRequestItems / this.pageJobRequestSize);
      },
      totalTimeSheetPages() {
        return Math.ceil(this.totalTimeSheetItems / this.pageTimeSheetSize);
      },
      startJobRequestIndex() {
        return (this.currentJobRequestPage - 1) * this.pageJobRequestSize;
      },
      startTimeSheetIndex() {
        return (this.currentTimeSheetPage - 1) * this.pageTimeSheetSize;
      },
      endJobRequestIndex() {
        return Math.min(this.startJobRequestIndex + this.pageTimeSheetSize - 1, this.totalJobRequestItems - 1);
      },
      endTimeSheetIndex() {
        return Math.min(this.startTimeSheetIndex + this.pageTimeSheetSize - 1, this.totalTimeSheetItems - 1);
      },
      pagesJobRequest() {
        let pagesJobRequest = [];
        for (let i = this.startJobRequestPage; i <= this.endJobRequestPage; i++) pagesJobRequest.push(i);
        return pagesJobRequest;
      },
      pagesTimeSheet() {
        let startTimeSheetPage = [];
        for (let i = this.startTimeSheetPage; i <= this.endTimeSheetPage; i++) startTimeSheetPage.push(i);
        return startTimeSheetPage;
      },
    },
});
