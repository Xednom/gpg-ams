Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#gpg-job-request',
  delimiters: ['[[',']]'],
  data: {
    jobRequests: [],
    statusOfTheJobRequests: [],
    projectManagers: [],
    loading: false,
    currentJobRequest: {},
    message: null,
    newJobRequest: {
      'date': null,
      'due_date': null,
      'client_code': null,
      'job_request_title': null,
      'job_request_sent_via': null,
      'job_request_instruction': null,
      'total_hours_minutes_allocated': null,
      'project_managers': null,
      'VA_admin_support': null,
      'status_of_the_job_request': null,
      'notes_and_coaching_from_project_manager': null,
    },
    search_term: ''
  },
  mounted: function() {
    this.getJobRequests();
    this.getStatusOfJobRequest();
    this.getProjectManagers();
  },
  methods: {
    reset: function() {
      this.newJobRequest.date =  this.newJobRequest.due_date = this.newJobRequest.client_code = null;
      this.newJobRequest.job_request_title = this.newJobRequest.job_request_sent_via = this.newJobRequest.job_request_instruction = null;
      this.newJobRequest.total_hours_minutes_allocated = this.newJobRequest.project_managers = this.newJobRequest.VA_admin_support = null;
      this.newJobRequest.status_of_the_job_request = this.newJobRequest.notes_and_coaching_from_project_manager = null;
    },
    getJobRequests: function() {
          let api_url = '/api/v1/jobrequest/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/v1/jobrequest/?search=${this.search_term}`
          }
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
    addJobRequest: function() {
      this.loading = true;
      this.$http.post('/api/v1/jobrequest/', this.newJobRequest)
          .then((response) => {
            this.loading = true;
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
            this.getClients();
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
  }
});
