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
    fetching: false,
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
    this.setDefaultDates();
    this.getProjectManagers();
    this.getJobRequestTitles();
    this.getJobTitle();
    this.getVAs();
    this.getClients();
    this.getProjectManagers();
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
      this.fetching = true;
      axios.get(`/api/v1/pms/`)
          .then((response) => {
            this.projectManagers = response.data;
            this.fetching = false;
          })
          .catch((err) => {
            this.fetching = false;
            console.log(err.response.data);
          })
    },
    getVAs: function () {
      this.fetching = true;
      axios.get(`/api/v1/vas/`)
        .then((response) => {
          this.virtualAssistants = response.data;
          this.fetching = false;
        })
        .catch((err) => {
          this.fetching = false;
          console.log(err.response.data);
        })
    },
    getClients: function () {
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
      this.saving = true
      axios.put(`/api/v1/jobrequest/${this.currentJobRequest.id}/`, this.currentJobRequest)
          .then((response) => {
            this.saving = false;
            this.currentJobRequest = response.data;
            swal({
              title: "GPG system",
              text: "Successfully updated the data!",
              icon: "success",
              button: false,
              timer: 1500
            })
            $("#editModal").modal("hide")
            this.getJobRequests();
          })
          .catch((err) => {
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
    },
    generateExcelFile: function () {
      let uri = 'data:application/vnd.ms-excel;base64,';

      let context = {
        worksheet: 'Worksheet1',
        header: this.htmlConverter(this.generateExcelHeader()),
        table: this.generateRows()
      }
      let htmlXML = this.generateXMLNS();
      let formattedTemplate = this.formatTemplate(htmlXML, context);
      let a = document.createElement('A');
      a.href = uri + this.base64(formattedTemplate);
      a.download = 'jobRequests-report-' + Date.now() + '.xlsx';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    },
    htmlConverter: function (data) {
      temporaryContainer = document.createElement('div');
      temporaryContainer.appendChild(data);

      return temporaryContainer.innerHTML
    },
    generateRows: function () {
      let jobRequests = this.jobRequests;
      let tableRows = '';

      for (let i = 0; i < jobRequests.length; i++) {
        tableRows += this.htmlConverter(
          this.generateData(jobRequests[i])
        );
      }

      return tableRows

    },
    generateData: function (jobRequests) {
      let tr = document.createElement('tr');

      let companyToRequest = document.createElement('td');
      let category = document.createElement('td');
      let dateRequested = document.createElement('td');
      let dueDate = document.createElement('td');
      let month = document.createElement('td');
      let requestorsName = document.createElement('td');
      let companyName = document.createElement('td');
      let jobRequestTitle = document.createElement('td');
      let jobRequestInstruction = document.createElement('td');
      let additionalCommentsOrFeedbacks = document.createElement('td');
      let assignedProjectManagers = document.createElement('td');
      let projectStatus = document.createElement('td');
      let urlTrainingVideos = document.createElement('td');
      let assignedVa = document.createElement('td');
      let managerNotes = document.createElement('td');
      let clientNotes = document.createElement('td');
      let vaNotes = document.createElement('td');
      let companyTagging = document.createElement('td');
      let authorizedMinutesHoursAllocation = document.createElement('td');

      companyToRequest.textContent = jobRequests['company_to_request'];
      category.textContent = jobRequests['category'];
      dateRequested.textContent = jobRequests['date_requested'];
      dueDate.textContent = jobRequests['due_date'];
      month.textContent = jobRequests['month'];
      requestorsName.textContent = jobRequests['requestors_name'];
      companyName.textContent = jobRequests['company_name'];
      jobRequestTitle.textContent = jobRequests['job_request_title'];
      jobRequestInstruction.textContent = jobRequests['job_request_instruction'];
      additionalCommentsOrFeedbacks.textContent = jobRequests['additional_comments_or_feedbacks'];
      assignedProjectManagers.textContent = jobRequests['assigned_project_managers'];
      projectStatus.textContent = jobRequests['project_status'];
      urlTrainingVideos.textContent = jobRequests['url_training_videos'];
      assignedVa.textContent = jobRequests['assigned_va'];
      managerNotes.textContent = jobRequests['manager_notes'];
      clientNotes.textContent = jobRequests['client_notes'];
      vaNotes.textContent = jobRequests['va_notes'];
      companyTagging.textContent = jobRequests['company_tagging'];
      authorizedMinutesHoursAllocation.textContent = jobRequests['authorized_minutes_hours_allocation'];

      tr.appendChild(companyToRequest);
      tr.appendChild(category);
      tr.appendChild(dateRequested);
      tr.appendChild(dueDate);
      tr.appendChild(month);
      tr.appendChild(requestorsName);
      tr.appendChild(companyName);
      tr.appendChild(jobRequestTitle);
      tr.appendChild(jobRequestInstruction);
      tr.appendChild(additionalCommentsOrFeedbacks);
      tr.appendChild(assignedProjectManagers);
      tr.appendChild(projectStatus);
      tr.appendChild(urlTrainingVideos);
      tr.appendChild(assignedVa);
      tr.appendChild(managerNotes);
      tr.appendChild(clientNotes);
      tr.appendChild(vaNotes);
      tr.appendChild(companyTagging);
      tr.appendChild(authorizedMinutesHoursAllocation);

      return tr
    },
    generateExcelHeader: function (jobRequests) {
      let tr = document.createElement('tr');

      let companyToRequest = document.createElement('th');
      let category = document.createElement('th');
      let dateRequested = document.createElement('th');
      let dueDate = document.createElement('th');
      let month = document.createElement('th');
      let requestorsName = document.createElement('th');
      let companyName = document.createElement('th');
      let jobRequestTitle = document.createElement('th');
      let jobRequestInstruction = document.createElement('th');
      let additionalCommentsOrFeedbacks = document.createElement('th');
      let assignedProjectManagers = document.createElement('th');
      let projectStatus = document.createElement('th');
      let urlTrainingVideos = document.createElement('th');
      let assignedVa = document.createElement('th');
      let managerNotes = document.createElement('th');
      let clientNotes = document.createElement('th');
      let vaNotes = document.createElement('th');
      let companyTagging = document.createElement('th');
      let authorizedMinutesHoursAllocation = document.createElement('th');

      companyToRequest.textContent = 'Company to Request';
      category.textContent = 'Category';
      dateRequested.textContent = 'Date Requested';
      dueDate.textContent = 'Due Date';
      month.textContent = 'Month';
      requestorsName.textContent = "Requestor's Name";
      companyName.textContent = 'Company name';
      jobRequestTitle.textContent = 'Job Request title';
      jobRequestInstruction.textContent = 'Job request Instruction';
      additionalCommentsOrFeedbacks.textContent = 'Additional Commnets or Feedbacks';
      assignedProjectManagers.textContent = 'Assigned Project Manager';
      projectStatus.textContent = 'Project Status';
      urlTrainingVideos.textContent = 'URL Training Videos';
      assignedVa.textContent = 'Assigned Va';
      managerNotes.textContent = 'Manager Notes';
      clientNotes.textContent = 'Client Notes';
      vaNotes.textContent = 'VA Notes';
      companyTagging.textContent = 'Company Tagging';
      authorizedMinutesHoursAllocation.textContent = 'Authorized Minues/Hours Allocation';

      tr.appendChild(companyToRequest);
      tr.appendChild(category);
      tr.appendChild(dateRequested);
      tr.appendChild(dueDate);
      tr.appendChild(month);
      tr.appendChild(requestorsName);
      tr.appendChild(companyName);
      tr.appendChild(jobRequestTitle);
      tr.appendChild(jobRequestInstruction);
      tr.appendChild(additionalCommentsOrFeedbacks);
      tr.appendChild(assignedProjectManagers);
      tr.appendChild(projectStatus);
      tr.appendChild(urlTrainingVideos);
      tr.appendChild(assignedVa);
      tr.appendChild(managerNotes);
      tr.appendChild(clientNotes);
      tr.appendChild(vaNotes);
      tr.appendChild(companyTagging);
      tr.appendChild(authorizedMinutesHoursAllocation);

      return tr
    },
    generateXMLNS: function () {
      let htmlOpenTag = '<html xmlns:o="urn:schemas-microsoft.com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">';
      let htmlHead = '<head><!-- [if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>{worksheet}</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--><meta http-equiv="content-type" content="text/plain; charset=UTF-8"></head>';
      let htmlBody = '<body><table>{header}{table}</table></body>';
      let htmlCloseTag = '</html>';

      return htmlOpenTag + htmlHead + htmlBody + htmlCloseTag;
    },
    base64: function (template) {
      return window.btoa(unescape(encodeURIComponent(template)))
    },
    formatTemplate: function (template, context) {
      return template.replace(/{(\w+)}/g, function (m, p) { return context[p] })
    },
    generatePDF: function (id, buttonNumber) {
      this.loadButton(buttonNumber);

      let link = document.createElement('a');
      link.href = `/land-master/${id}/jobRequests-report.pdf`;
      link.download = 'marketing-sites-jobRequests-Report-' + Date.now();
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    },
    loadButton: function (buttonNumber) {
      Vue.set(this.buttonsLoading, buttonNumber, 1);

      let self = this;

      setTimeout(function () {
        Vue.set(self.buttonsLoading, buttonNumber, 0);
      }, 8000);
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
