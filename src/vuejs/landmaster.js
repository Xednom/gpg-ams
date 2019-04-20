Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-land-master',
    delimiters: ['[[',']]'],
    data: {
        loading: false,
        saving: false,
        dueDiligences: [],
        clientNames: [],
        virtualAssistants: [],
        projectManagers: [],
        currentDueDiligence: [],
        newDueDiligence: {
            'date_requested': null,
            'company_name': "",
            'company_owner_or_requestor': "",
            'due_date': null,
            'owner_name': "",
            'parcel_number': "",
            'account_number': "",
            'property_address': "",
            'county': "",
            'lot_number': "",
            'legal_description': "",
            'parcel_size': "",
            'gps_coordinates': "",
            'gps_coordinates_4_corners': "",
            'google_map_link': "",
            'elevation': "",
            'assessed_value': "",
            'access_to_property': "",
            'closest_major_city': "",
            'closest_small_town': "",
            'nearby_attractions': "",
            'assessor_website': "",
            'treasurer_website': "",
            'recorder_clerk_website': "",
            'zoning_department_website': "",
            'gis_website': "",
            'cad_website': "",
            'planning_department_contact': "",
            'recorder_clerk_contact': "",
            'tax_office_contact': "",
            'assessors_office_contact': "",
            'back_taxes': "",
            'tax_liens': "",
            'annual_property_taxes': "",
            'is_property_part_of_an_hoa': "",
            'how_much_dues': "",
            'zoning': "",
            'terrian_type': "",
            'property_use_code': "",
            'what_can_be_built': "",
            'time_limit_to_build': "",
            'can_camp': "",
            'notes_on_camping': "",
            'rv_allowed': "",
            'note_on_rv': "",
            'mobile_homes': "",
            'notes_on_mobile_homes': "",
            'is_property_flood_zone_area': "",
            'water': "",
            'sewer_or_septic': "",
            'power': "",
            'gas': "",
            'waste': "",
            'date_completed': "",
            'notes_from_the_client': "",
            'notes_from_the_quality_specialist': "",
            'notes_from_the_virtual_assistant': "",
            'dd_team_assigned_va': "",
            'project_manager': "",
            'total_minutes_hours_duration': "",
            'attachments': "",
            'status_of_dd': "",
        },
        // for pagination
        currentPage: 1,
        pageSize: RECORDS_PER_PAGE,
        startPage: 1,
        endPage: null,
        maxPages: RECORDS_PER_PAGE,
        paginatedRecords: [],
    },
    mounted: function () {
        this.getClientNames();
        this.getDueDiligences();
        this.getVas();
        this.getProjectManagers();
    },
    methods: {
        resetDueDiligenceFields: function () {
            Object.keys(this.newDueDiligence).forEach(key => {
                this.newDueDiligence[key] = ""
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
        getVas: function () {
            this.loading = true;
            this.$http.get(`/api/v1/virtual-assistant`)
                .then((response) =>{
                    this.virtualAssistants = response.data;
                    this.loading = false;
                })
                .catch((err) =>{
                    this.loading = false;
                    console.log(err);
                })
        },
        getProjectManagers: function () {
            this.loading = true;
            this.$http.get(`/api/v1/project-manager`)
                .then((response) => {
                    this.projectManagers = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addDueDiligence: function () {
            this.saving = true;
            this.$http.post('/api/v1/due-diligence/', this.newDueDiligence)
                .then((response) => {
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: "Due Diligence task has been added successfully!",
                        icon: "success",
                        buttons: false,
                        timer: 3000
                    }).then(function() {
                    window.location.reload()
                    });
                    this.resetDueDiligenceFields();
                })
                .catch((err) => {
                    this.saving = false;
                    console.log(err);
                })
        },
        updateDueDiligence: function () {
            this.loading = true;
            this.$http.put(`/api/v1/due-diligence/${this.currentDueDiligence.id}/`, this.currentDueDiligence)
                .then((response) => {
                    this.loading = false;
                    this.currentDueDiligence = response.data;
                    swal({
                        title: "GPG system",
                        text: "Successfully updated the data!",
                        icon: "success",
                        button: false,
                        timer: 1500
                    });
                    $("#editModal").modal('hide')
                    this.getDueDiligences();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getDueDiligences: function () {
            this.loading = true;
            this.$http.get(`/api/v1/due-diligence/`)
                .then((response) => {
                    this.loading = false;
                    this.dueDiligences = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        viewDueDiligence: function (id) {
            this.loading = true;
            this.$http.get(`/api/v1/due-diligence/${id}/`)
                .then((response) => {
                    this.loading = false;
                    this.currentDueDiligence = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getPaginatedRecords: function () {
                const startIndex = this.startIndex;
                this.paginatedRecords = this.dueDiligences.slice().splice(startIndex, this.pageSize);
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
            dueDiligences: function (newDueDiligencesRecords, oldDueDiligencesRecords) {
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
                return this.dueDiligences.length;
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