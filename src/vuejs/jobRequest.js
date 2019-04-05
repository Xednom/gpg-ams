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
    loading: false,
    saving: false,
    currentJobRequest: {},
    message: null,
    newJobRequest: {
      'category': null,
      'date_requested': null,
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
      'total_minutes_hours': null,
      'manager_notes': null,
      'client_notes': null,
      'va_notes': null,
      'company_billable_to': null,
      'company_asigned_to': null,
    },
    search_term: ''
  },
  mounted: function() {
    this.getJobRequests();
    //this.getStatusOfJobRequest();
    this.getProjectManagers();
    this.getJobRequestTitles();
    this.getVAs();
  },
  methods: {
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
      this.$http.get(`/api/v1/project-manager/`)
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
            this.loading = true;
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

    }
  }
});
