Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#gpg',
  delimiters: ['[[',']]'],
  data: {
    clients: [],
    clientNames:[],
    clientProjectManagers: [],
    clientSeniorManagers: [],
    clientStatus: [],
    loading: false,
    currentClient: {},
    currentClientName: {},
    message: null,
    newClient: {
      'client_company_name': null,
      'client_code': null,
      'company_name': null,
      'client_phone_number': null,
      'client_email': null,
      'clients_project_manager': null,
      'senior_manager': null,
      'VA_assigned': null,
      'type_of_task': null,
      'status': null,
      'notes': null,
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
    this.getClients();
    this.getClientNames();
    this.getClientProjectManagers();
    this.getClientSeniorManagers();
    // this.getClientVA();
    // this.getClientStatus();
  },
  methods: {
    getClients: function() {
          let api_url = '/api/v1/client/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/v1/client/?search=${this.search_term}`
          }
          this.loading = true;
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
    },
    getPaginatedRecords: function() {
      const startIndex = this.startIndex;
      this.paginatedRecords = this.clients.slice().splice(startIndex, this.pageSize);
    },
    goToPage: function(page) {
      if(page < 1) {
        return this.currentPage = 1;
      }
      if(page > this.totalPages) {
        return this.currentPage = this.totalPages;
      }
      this.currentPage = page;
    },
    setPageGroup: function() {
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
    }
  },
  watch: {
    clients: function(newClientRecords, oldClientRecords) {
      this.setPageGroup();
      this.getPaginatedRecords();
    },
    currentPage: function(newCurrenPage, oldCurrentPage) {
      this.setPageGroup();
      this.getPaginatedRecords();
    },
  },
  computed: {
    totalItems: function() {
      return this.clients.length;
    },
    totalPages: function() {
      return Math.ceil(this.totalItems / this.pageSize);
    },
    startIndex: function() {
      return (this.currentPage - 1) * this.pageSize;
    },
    endIndex: function() {
      return Math.min(this.startIndex + this.pageSize - 1, this.totalItems - 1);
    },
    pages: function() {
      let pages = [];
      for (let i = this.startPage; i <= this.endPage; i++) pages.push(i);
      return pages;
    },
  }
});
