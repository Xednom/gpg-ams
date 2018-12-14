Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#gpg',
  delimiters: ['[[',']]'],
  data: {
    clients: [],
    clientNames:[],
    clientProjectManagers: [],
    clientSeniorManagers: [],
    clientVA: [],
    clientStatus: [],
    loading: false,
    currentClient: {},
    currentClientName: {},
    message: null,
    newClient: {
      'clients_company_name': null,
      'client_code': null,
      'client': null,
      'client_phone_number': null,
      'client_email': null,
      'clients_project_manager': null,
      'senior_manager': null,
      'VA_assigned': null,
      'type_of_task': null,
      'status': null,
      'notes': null,
    },
    search_term: ''
  },
  mounted: function() {
    this.getClients();
    this.getClientNames();
    this.getClientProjectManagers();
    this.getClientSeniorManagers();
    this.getClientVA();
    // this.getClientStatus();
  },
  methods: {
    getClients: function() {
          let api_url = '/api/v1/client/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/v1/client/?search=${this.search_term}`
          }
          this.loading = false;
          this.$http.get(api_url)
              .then((response) => {
                this.clients = response.data;
                this.loading = false;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },
    getClient: function(id) {
      this.loading = true;
      this.$http.get(`/api/v1/client/${id}/`)
          .then((response) => {
            this.currentClient = response.data;
            $('#editItemModal').modal('show');
            this.loading = false;
            $("#editItemModal").modal('hide');
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getClientNames: function() {
      this.loading = true;
      this.$http.get(`/api/v1/client-name/`)
          .then((response) => {
            this.clientNames = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getClientProjectManagers: function() {
      this.loading = true;
      this.$http.get(`/api/v1/project-manager/`)
          .then((response) => {
            this.clientProjectManagers = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getClientSeniorManagers: function() {
      this.loading = true;
      this.$http.get(`/api/v1/senior-manager/`)
          .then((response) => {
            this.clientSeniorManagers = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getClientVA: function() {
      this.loading = true;
      this.$http.get(`/api/v1/custom-user/`)
          .then((response) => {
            this.clientVA = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    // getClientStatus: function() {
    //   this.loading = true;
    //   this.$http.get(`/api/v1/status-choice/`)
    //       .then((response) => {
    //         this.clientStatus = response.data;
    //         this.loading = false;
    //       })
    //       .catch((err) => {
    //         this.loading = false;
    //         console.log(err);
    //       })
    // },
    addClient: function() {
      this.loading = true;
      this.$http.post('/api/v1/client/', this.newItem)
          .then((response) => {
            this.loading = true;
            $("#addItemModal").modal('hide');
            $(".modal-backdrop").remove();
            swal({
              title: "GPG System",
              text: "Data has been saved successfully",
              icon: "success",
              buttons: false,
              timer: 1500
            })
            this.getItems();
          })
          .catch((err) => {
            this.loading = true;
            console.log(err);
          })
    },
    updateClient: function() {
      this.loading = true;
      this.$http.put(`/api/v1/client/${this.currentClient.id}/`, this.currentClient)
          .then((response) => {
            this.loading = false;
            this.currentClient = response.data;
            // after updating hide the modal
            $("#editModal").modal('hide');
            $(".modal-backdrop").remove();
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
    deleteClient: function(id) {
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
          this.$http.delete(`/api/v1/client/${id}/`)
              .then((response) => {
                this.loading = false;
                this.getClients();
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
