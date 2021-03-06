Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
new Vue({
    el: '#gpg-land-master',
    delimiters: ['[[', ']]'],
    data: {
        loading: false,
        viewing: false,
        saving: false,
        errored: false,
        fetching: false,
        dueDiligences: [],
        clients: [],
        virtualAssistants: [],
        projectManagers: [],
        currentDueDiligence: [],
        buttonsLoading: [],
        errorduediligence: [],
        currentSort: '',
        currentSortDir: 'desc',
        newDueDiligence: {
            'date_requested': null,
            'company_name': "",
            'company_owner_or_requestor': "",
            'due_date': null,
            'county_operator_details': "",
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
            'notes_from_the_client': "",
            'notes_from_the_quality_specialist': "",
            'notes_from_the_virtual_assistant': "",
            'notes_on_zoning': "",
            'notes_on_utilities': "",
            'notes_on_tax': "",
            'notes_on_legal_description': "",
            'notes_on_deeds': "",
            'dd_va_assigned_initial_data': "",
            'dd_va_assigned_call_outs_tax_data': "",
            'dd_va_assigned_call_outs_zoning_data': "",
            'dd_va_assigned_call_outs_utilities_data': "",
            'dd_va_assigned_call_outs_other_requests': "",
            'project_manager': "",
            'attachments': "",
            'status_of_dd': "",
            'leve_of_urgency': "",
            'initial_due_diligence_completion': null,
            'tax_data_completion': null,
            'zoning_data_completion': null,
            'utilities_data_completion': null,
            'other_requests_completion': null,
            'date_of_completion': null,
            'operator_details_tax_data': "",
            'operator_details_zoning_data': "",
            'operator_details_utilities_data': "",
            'operator_details_other_requests': "",
            'status_initial_data': "",
            'status_tax_data': "",
            'status_zoning_data': "",
            'status_utilities_data': "",
            'status_other_requests': "",
            'status_tax_data': "",
            'total_hrs_for_initial_dd': 0.00,
            'total_hrs_overall_dd_callouts': 0.00,
            'subdivision': "",
            'parcel_dimensions': "",
            'structure': "",
            'no_address': "",
            'liens_on_property': "",
            'tax_amount': "",
            'land_cleared': "",
            'property_buildable': "",
            'hoa': "",
            'city_or_mud_district': "",
            'water_connected': "",
            'water_to_property': "",
            'electricity_connected': "",
            'no_power': "",
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
        $('#datetimepickerinitialtimein').datetimepicker({
            format: "YYYY-MM-DD HH:mm"
        });
        $('#datetimepickerinitialtimeout').datetimepicker({
            format: "YYYY-MM-DD HH:mm"
        });
    },
    methods: {
        numberInputsOnly($event) {
            // console.log($event.keyCode); //keyCodes value
            let keyCode = ($event.keyCode ? $event.keyCode : $event.which);

            // only allow number and one dot
            if ((keyCode < 48 || keyCode > 57) && (keyCode !== 46 || this.price.indexOf('.') != -1)) { // 46 is dot
                $event.preventDefault();
            }

            // restrict to 2 decimal places
            if (this.price != null && this.price.indexOf(".") > -1 && (this.price.split('.')[1].length > 1)) {
                $event.preventDefault();
            }
        },
        sort: function (s) {
            //if s == current sort, reverse
            if (s === this.currentSort) {
                this.currentSortDir = this.currentSortDir === 'asc' ? 'desc' : 'asc';
            }
            this.currentSort = s;
        },
        resetDueDiligenceFields: function () {
            Object.keys(this.newDueDiligence).forEach(key => {
                this.newDueDiligence[key] = ""
            })
        },
        getClientNames() {
            this.loading = true;
            axios.get(`/api/v1/client/`)
                .then((response) => {
                    this.clients = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        getVas: function () {
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
        getProjectManagers: function () {
            this.loading = true;
            axios.get(`/api/v1/pms`)
                .then((response) => {
                    this.projectManagers = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        addDueDiligence: function () {
            this.saving = true;
            axios.post('/api/v1/due-diligence/', this.newDueDiligence)
                .then((response) => {
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: "Due Diligence task has been added successfully!",
                        icon: "success",
                        buttons: false,
                        timer: 3000
                    }).then(function () {
                        window.location.reload()
                    });
                    this.resetDueDiligenceFields();
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
                    console.log(err.response.data);
                })
        },
        updateDueDiligence: function () {
            this.saving = true;
            axios.put(`/api/v1/due-diligence/${this.currentDueDiligence.id}/`, this.currentDueDiligence)
                .then((response) => {
                    this.saving = false;
                    this.currentDueDiligence = response.data;
                    console.log(this.currentDueDiligence.date_completed_initial_dd_time_in);
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
                    this.saving = false;
                    swal({
                        title: "GPG System",
                        text: JSON.stringify(err.body),
                        icon: "error",
                        buttons: false,
                        timer: 3000,
                    });
                    console.log(err.response.data);
                })
        },
        getDueDiligences: function () {
            this.loading = true;
            axios.get(`/api/v1/due-diligence/`)
                .then((response) => {
                    this.loading = false;
                    this.dueDiligences = response.data;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err.response.data);
                })
        },
        viewDueDiligence: function (id) {
            this.viewing = true;
            axios.get(`/api/v1/due-diligence/${id}/`)
                .then((response) => {
                    this.viewing = false;
                    this.currentDueDiligence = response.data;
                })
                .catch((err) => {
                    this.viewing = false;
                    console.log(err.response.data);
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
            a.download = 'due-diligence-Report-' + Date.now() + '.xlsx';
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
            let duediligences = this.dueDiligences;
            let tableRows = '';

            for (let i = 0; i < duediligences.length; i++) {
                tableRows += this.htmlConverter(
                    this.generateData(duediligences[i])
                );
            }

            return tableRows

        },
        generateData: function (duediligence) {
            let tr = document.createElement('tr');

            let dateRequested = document.createElement('td');
            let companyName = document.createElement('td');
            let companyOwnerOrRequestor = document.createElement('td');
            let dueDate = document.createElement('td');
            let customerCare = document.createElement('td');
            let ownerName = document.createElement('td');
            let parcelNumber = document.createElement('td');
            let accountNumber = document.createElement('td');
            let propertyAddress = document.createElement('td');
            let county = document.createElement('td');
            let lotNumber = document.createElement('td');
            let legalDescription = document.createElement('td');
            let parcelSize = document.createElement('td');
            let gpsCoordinates = document.createElement('td');
            let gpsCoordinates4Corners = document.createElement('td');
            let googleMapLink = document.createElement('td');
            let elevation = document.createElement('td');
            let assessedValue = document.createElement('td');
            let accessToProperty = document.createElement('td');
            let closestMajorCity = document.createElement('td');
            let closestSmallTown = document.createElement('td');
            let nearbyAttractions = document.createElement('td');
            let assessorWebsite = document.createElement('td');
            let treasurerWebsite = document.createElement('td');
            let reorderClerkWebsite = document.createElement('td');
            let zoningDepartmentWebsite = document.createElement('td');
            let gisWebsite = document.createElement('td');
            let cadWebsite = document.createElement('td');
            let planningDepartmentContact = document.createElement('td');
            let recorderClerkContact = document.createElement('td');
            let taxOfficeContact = document.createElement('td');
            let assessorsOfficeContact = document.createElement('td');
            let backTaxes = document.createElement('td');
            let taxLiens = document.createElement('td');
            let annualPropertyTaxes = document.createElement('td');
            let isPropertyPartOfAnHoa = document.createElement('td');
            let howMuchDues = document.createElement('td');
            let zoning = document.createElement('td');
            let terrianType = document.createElement('td');
            let propertyUseCode = document.createElement('td');
            let whatCanBeBuilt = document.createElement('td');
            let timeLimitToBuild = document.createElement('td');
            let canCamp = document.createElement('td');
            let notesOnCamping = document.createElement('td');
            let rvAllowed = document.createElement('td');
            let noteOnRv = document.createElement('td');
            let mobileHomes = document.createElement('td');
            let notesOnMobileHomes = document.createElement('td');
            let isPropertyFloodZoneArea = document.createElement('td');
            let water = document.createElement('td');
            let sewerOrSeptic = document.createElement('td');
            let power = document.createElement('td');
            let gas = document.createElement('td');
            let waste = document.createElement('td');
            let dateCompleted = document.createElement('td');
            let notesFromTheClient = document.createElement('td');
            let notesFromTheQualitySpecialist = document.createElement('td');
            let notesFromTheVirtualAssistant = document.createElement('td');
            let notesOnZoning = document.createElement('td');
            let notesOnUtilities = document.createElement('td');
            let notesOnTax = document.createElement('td');
            let notesOnLegalDescription = document.createElement('td');
            let notesOnDeeds = document.createElement('td');
            let ddVaAssignedInitialData = document.createElement('td');
            let ddVaAssignedCallsOutsTaxData = document.createElement('td');
            let ddVaAssignedCallsOutsZoningData = document.createElement('td');
            let ddVaAssignedCallsOutsUtilitiesData = document.createElement('td');
            let ddVaAssignedCallsOutsOtherRequest = document.createElement('td');
            let projectManager = document.createElement('td');
            let statusOfDd = document.createElement('td');
            let initialDueDiligenceCompletion = document.createElement('td');
            let taxDataCompletion = document.createElement('td');
            let zoningDataCompletion = document.createElement('td');
            let utilitiesDataCompletion = document.createElement('td');
            let otherRequestsCompletion = document.createElement('td');
            let dateOfCompletion = document.createElement('td');
            let operatorDetailsTaxData = document.createElement('td');
            let operatorDetailsZoningData = document.createElement('td');
            let operatorDetailsUtilitiesData = document.createElement('td');
            let operatorDetailsOtherRequests = document.createElement('td');
            let statusInitialData = document.createElement('td');
            let statusTaxData = document.createElement('td');
            let statusZoningData = document.createElement('td');
            let statusUtilitiesData = document.createElement('td');
            let statusOtherRequests = document.createElement('td');
            let levelOfUrgency = document.createElement('td');

            dateRequested.textContent = duediligence['date_requested'];
            companyName.textContent = duediligence['company_name'];
            companyOwnerOrRequestor.textContent = duediligence['company_owner_or_requestor'];
            dueDate.textContent = duediligence['due_date'];
            customerCare.textContent = duediligence['customer_care_specialist'];
            ownerName.textContent = duediligence['owner_name'];
            parcelNumber.textContent = duediligence['parcel_number'];
            accountNumber.textContent = duediligence['account_number'];
            propertyAddress.textContent = duediligence['property_address'];
            county.textContent = duediligence['county'];
            lotNumber.textContent = duediligence['lot_number'];
            legalDescription.textContent = duediligence['legal_description'];
            parcelSize.textContent = duediligence['parcel_size'];
            gpsCoordinates.textContent = duediligence['gps_coordinates'];
            gpsCoordinates4Corners.textContent = duediligence['gps_coordinates_4_corners'];
            googleMapLink.textContent = duediligence['google_map_link'];
            elevation.textContent = duediligence['elevation'];
            assessedValue.textContent = duediligence['assessed_value'];
            accessToProperty.textContent = duediligence['access_to_property'];
            closestMajorCity.textContent = duediligence['closest_major_city'];
            closestSmallTown.textContent = duediligence['closest_small_town'];
            nearbyAttractions.textContent = duediligence['nearby_attractions'];
            assessorWebsite.textContent = duediligence['assessor_website'];
            treasurerWebsite.textContent = duediligence['treasurer_website'];
            reorderClerkWebsite.textContent = duediligence['recorder_clerk_website'];
            zoningDepartmentWebsite.textContent = duediligence['zoning_department_website'];
            gisWebsite.textContent = duediligence['gis_website'];
            cadWebsite.textContent = duediligence['cad_website'];
            planningDepartmentContact.textContent = duediligence['planning_department_contact'];
            recorderClerkContact.textContent = duediligence['recorder_clerk_contact'];
            taxOfficeContact.textContent = duediligence['tax_office_contact'];
            assessorsOfficeContact.textContent = duediligence['assessors_office_contact'];
            backTaxes.textContent = duediligence['back_taxes'];
            taxLiens.textContent = duediligence['tax_liens'];
            annualPropertyTaxes.textContent = duediligence['annual_property_taxes'];
            isPropertyPartOfAnHoa.textContent = duediligence['is_property_part_of_an_hoa'];
            howMuchDues.textContent = duediligence['how_much_dues'];
            zoning.textContent = duediligence['zoning'];
            terrianType.textContent = duediligence['terrian_type'];
            propertyUseCode.textContent = duediligence['property_use_code'];
            whatCanBeBuilt.textContent = duediligence['what_can_be_built'];
            timeLimitToBuild.textContent = duediligence['time_limit_to_build'];
            canCamp.textContent = duediligence['can_camp'];
            notesOnCamping.textContent = duediligence['notes_on_camping'];
            rvAllowed.textContent = duediligence['rv_allowed'];
            noteOnRv.textContent = duediligence['note_on_rv'];
            mobileHomes.textContent = duediligence['mobile_homes'];
            notesOnMobileHomes.textContent = duediligence['notes_on_mobile_homes'];
            isPropertyFloodZoneArea.textContent = duediligence['is_property_flood_zone_area'];
            water.textContent = duediligence['water'];
            sewerOrSeptic.textContent = duediligence['sewer_or_septic'];
            power.textContent = duediligence['power'];
            gas.textContent = duediligence['gas'];
            waste.textContent = duediligence['waste'];
            dateCompleted.textContent = duediligence['date_completed'];
            notesFromTheClient.textContent = duediligence['notes_from_the_client'];
            notesFromTheQualitySpecialist.textContent = duediligence['notes_from_the_quality_specialist'];
            notesFromTheVirtualAssistant.textContent = duediligence['notes_from_the_virtual_assistant'];
            notesOnZoning.textContent = duediligence['notes_on_zoning'];
            notesOnUtilities.textContent = duediligence['notes_on_utilities'];
            notesOnTax.textContent = duediligence['notes_on_tax'];
            notesOnLegalDescription.textContent = duediligence['notes_on_legal_description'];
            notesOnDeeds.textContent = duediligence['notes_on_deeds'];
            ddVaAssignedInitialData.textContent = duediligence['dd_va_assigned_initial_data'];
            ddVaAssignedCallsOutsTaxData.textContent = duediligence['dd_va_assigned_call_outs_tax_data'];
            ddVaAssignedCallsOutsZoningData.textContent = duediligence['dd_va_assigned_call_outs_zoning_data'];
            ddVaAssignedCallsOutsUtilitiesData.textContent = duediligence['dd_va_assigned_call_outs_utilities_data'];
            ddVaAssignedCallsOutsOtherRequest.textContent = duediligence['dd_va_assigned_call_outs_other_requests'];
            projectManager.textContent = duediligence['project_manager'];
            statusOfDd.textContent = duediligence['status_of_dd'];
            initialDueDiligenceCompletion.textContent = duediligence['initial_due_diligence_completion'];
            taxDataCompletion.textContent = duediligence['tax_data_completion'];
            zoningDataCompletion.textContent = duediligence['zoning_data_completion'];
            utilitiesDataCompletion.textContent = duediligence['utilities_data_completion'];
            otherRequestsCompletion.textContent = duediligence['other_requests_completion'];
            dateOfCompletion.textContent = duediligence['date_of_completion'];
            operatorDetailsTaxData.textContent = duediligence['operator_details_tax_data'];
            operatorDetailsZoningData.textContent = duediligence['operator_details_zoning_data'];
            operatorDetailsUtilitiesData.textContent = duediligence['operator_details_utilities_data'];
            operatorDetailsOtherRequests.textContent = duediligence['operator_details_other_requests'];
            statusInitialData.textContent = duediligence['status_initial_data'];
            statusTaxData.textContent = duediligence['status_tax_data'];
            statusZoningData.textContent = duediligence['status_zoning_data'];
            statusUtilitiesData.textContent = duediligence['status_utilities_data'];
            statusOtherRequests.textContent = duediligence['status_other_requests'];
            levelOfUrgency.textContent = duediligence['level_of_urgency'];

            tr.appendChild(dateRequested);
            tr.appendChild(companyName);
            tr.appendChild(companyOwnerOrRequestor);
            tr.appendChild(dueDate);
            tr.appendChild(customerCare);
            tr.appendChild(ownerName);
            tr.appendChild(parcelNumber);
            tr.appendChild(accountNumber);
            tr.appendChild(propertyAddress);
            tr.appendChild(county);
            tr.appendChild(lotNumber);
            tr.appendChild(legalDescription);
            tr.appendChild(parcelSize);
            tr.appendChild(gpsCoordinates);
            tr.appendChild(gpsCoordinates4Corners);
            tr.appendChild(googleMapLink);
            tr.appendChild(elevation);
            tr.appendChild(assessedValue);
            tr.appendChild(accessToProperty);
            tr.appendChild(closestMajorCity);
            tr.appendChild(closestSmallTown);
            tr.appendChild(nearbyAttractions);
            tr.appendChild(assessorWebsite);
            tr.appendChild(treasurerWebsite);
            tr.appendChild(reorderClerkWebsite);
            tr.appendChild(zoningDepartmentWebsite);
            tr.appendChild(gisWebsite);
            tr.appendChild(cadWebsite);
            tr.appendChild(planningDepartmentContact);
            tr.appendChild(recorderClerkContact);
            tr.appendChild(taxOfficeContact);
            tr.appendChild(assessorsOfficeContact);
            tr.appendChild(backTaxes);
            tr.appendChild(taxLiens);
            tr.appendChild(annualPropertyTaxes);
            tr.appendChild(isPropertyPartOfAnHoa);
            tr.appendChild(howMuchDues);
            tr.appendChild(zoning);
            tr.appendChild(terrianType);
            tr.appendChild(propertyUseCode);
            tr.appendChild(whatCanBeBuilt);
            tr.appendChild(timeLimitToBuild);
            tr.appendChild(canCamp);
            tr.appendChild(notesOnCamping);
            tr.appendChild(rvAllowed);
            tr.appendChild(noteOnRv);
            tr.appendChild(mobileHomes);
            tr.appendChild(notesOnMobileHomes);
            tr.appendChild(isPropertyFloodZoneArea);
            tr.appendChild(water);
            tr.appendChild(sewerOrSeptic);
            tr.appendChild(power);
            tr.appendChild(gas);
            tr.appendChild(waste);
            tr.appendChild(dateCompleted);
            tr.appendChild(notesFromTheClient);
            tr.appendChild(notesFromTheQualitySpecialist);
            tr.appendChild(notesFromTheVirtualAssistant);
            tr.appendChild(notesOnUtilities);
            tr.appendChild(notesOnTax);
            tr.appendChild(notesOnLegalDescription);
            tr.appendChild(notesOnDeeds);
            tr.appendChild(ddVaAssignedInitialData);
            tr.appendChild(ddVaAssignedCallsOutsTaxData);
            tr.appendChild(ddVaAssignedCallsOutsZoningData);
            tr.appendChild(ddVaAssignedCallsOutsUtilitiesData);
            tr.appendChild(ddVaAssignedCallsOutsOtherRequest);
            tr.appendChild(projectManager);
            tr.appendChild(statusOfDd);
            tr.appendChild(initialDueDiligenceCompletion);
            tr.appendChild(taxDataCompletion);
            tr.appendChild(zoningDataCompletion);
            tr.appendChild(utilitiesDataCompletion);
            tr.appendChild(otherRequestsCompletion);
            tr.appendChild(dateOfCompletion);
            tr.appendChild(operatorDetailsTaxData);
            tr.appendChild(operatorDetailsZoningData);
            tr.appendChild(operatorDetailsUtilitiesData);
            tr.appendChild(operatorDetailsOtherRequests);
            tr.appendChild(statusInitialData);
            tr.appendChild(statusTaxData);
            tr.appendChild(statusZoningData);
            tr.appendChild(statusUtilitiesData);
            tr.appendChild(statusOtherRequests);
            tr.appendChild(levelOfUrgency);

            return tr
        },
        generateExcelHeader: function (duediligence) {
            let tr = document.createElement('tr');

            let dateRequested = document.createElement('th');
            let companyName = document.createElement('th');
            let companyOwnerOrRequestor = document.createElement('th');
            let dueDate = document.createElement('th');
            let customerCare = document.createElement('th');
            let ownerName = document.createElement('th');
            let parcelNumber = document.createElement('th');
            let accountNumber = document.createElement('th');
            let propertyAddress = document.createElement('th');
            let county = document.createElement('th');
            let lotNumber = document.createElement('th');
            let legalDescription = document.createElement('th');
            let parcelSize = document.createElement('th');
            let gpsCoordinates = document.createElement('th');
            let gpsCoordinates4Corners = document.createElement('th');
            let googleMapLink = document.createElement('th');
            let elevation = document.createElement('th');
            let assessedValue = document.createElement('th');
            let accessToProperty = document.createElement('th');
            let closestMajorCity = document.createElement('th');
            let closestSmallTown = document.createElement('th');
            let nearbyAttractions = document.createElement('th');
            let assessorWebsite = document.createElement('th');
            let treasurerWebsite = document.createElement('th');
            let reorderClerkWebsite = document.createElement('th');
            let zoningDepartmentWebsite = document.createElement('th');
            let gisWebsite = document.createElement('th');
            let cadWebsite = document.createElement('th');
            let planningDepartmentContact = document.createElement('th');
            let recorderClerkContact = document.createElement('th');
            let taxOfficeContact = document.createElement('th');
            let assessorsOfficeContact = document.createElement('th');
            let backTaxes = document.createElement('th');
            let taxLiens = document.createElement('th');
            let annualPropertyTaxes = document.createElement('th');
            let isPropertyPartOfAnHoa = document.createElement('th');
            let howMuchDues = document.createElement('th');
            let zoning = document.createElement('th');
            let terrianType = document.createElement('th');
            let propertyUseCode = document.createElement('th');
            let whatCanBeBuilt = document.createElement('th');
            let timeLimitToBuild = document.createElement('th');
            let canCamp = document.createElement('th');
            let notesOnCamping = document.createElement('th');
            let rvAllowed = document.createElement('th');
            let noteOnRv = document.createElement('th');
            let mobileHomes = document.createElement('th');
            let notesOnMobileHomes = document.createElement('th');
            let isPropertyFloodZoneArea = document.createElement('th');
            let water = document.createElement('th');
            let sewerOrSeptic = document.createElement('th');
            let power = document.createElement('th');
            let gas = document.createElement('th');
            let waste = document.createElement('th');
            let dateCompleted = document.createElement('th');
            let notesFromTheClient = document.createElement('th');
            let notesFromTheQualitySpecialist = document.createElement('th');
            let notesFromTheVirtualAssistant = document.createElement('th');
            let notesOnUtilities = document.createElement('th');
            let notesOnTax = document.createElement('th');
            let notesOnLegalDescription = document.createElement('th');
            let notesOnDeeds = document.createElement('th');
            let ddVaAssignedInitialData = document.createElement('th');
            let ddVaAssignedCallsOutsTaxData = document.createElement('th');
            let ddVaAssignedCallsOutsZoningData = document.createElement('th');
            let ddVaAssignedCallsOutsUtilitiesData = document.createElement('th');
            let ddVaAssignedCallsOutsOtherRequest = document.createElement('th');
            let projectManager = document.createElement('th');
            let statusOfDd = document.createElement('th');
            let initialDueDiligenceCompletion = document.createElement('th');
            let taxDataCompletion = document.createElement('th');
            let zoningDataCompletion = document.createElement('th');
            let utilitiesDataCompletion = document.createElement('th');
            let otherRequestsCompletion = document.createElement('th');
            let dateOfCompletion = document.createElement('th');
            let operatorDetailsTaxData = document.createElement('th');
            let operatorDetailsZoningData = document.createElement('th');
            let operatorDetailsUtilitiesData = document.createElement('th');
            let operatorDetailsOtherRequests = document.createElement('th');
            let statusInitialData = document.createElement('th');
            let statusTaxData = document.createElement('th');
            let statusZoningData = document.createElement('th');
            let statusUtilitiesData = document.createElement('th');
            let statusOtherRequests = document.createElement('th');
            let levelOfUrgency = document.createElement('th');

            dateRequested.textContent = 'Date Requested';
            companyName.textContent = 'Company Name';
            companyOwnerOrRequestor.textContent = 'Company Owner or Requestor';
            dueDate.textContent = 'Due Date';
            customerCare.textContent = 'Customer Care Specialist';
            ownerName.textContent = 'Owner Name';
            parcelNumber.textContent = 'Parcel Number';
            accountNumber.textContent = 'Account Number';
            propertyAddress.textContent = 'Property Address';
            county.textContent = 'County';
            lotNumber.textContent = 'Lot Number';
            legalDescription.textContent = 'Legal Description';
            parcelSize.textContent = 'Parcel Size';
            gpsCoordinates.textContent = 'GPS Coordinates';
            gpsCoordinates4Corners.textContent = 'GPS Coordinates 4 Corners';
            googleMapLink.textContent = 'Google Map Link';
            elevation.textContent = 'Elevation';
            assessedValue.textContent = 'Assessed Value';
            accessToProperty.textContent = 'Access To Property';
            closestMajorCity.textContent = 'Closest Major City';
            closestSmallTown.textContent = 'Closest Small Town';
            nearbyAttractions.textContent = 'Nearby Attractions';
            assessorWebsite.textContent = 'Assessor Website';
            treasurerWebsite.textContent = 'Treasurer Website';
            reorderClerkWebsite.textContent = 'Reorder Clerk Website';
            zoningDepartmentWebsite.textContent = 'Zoning Department Website';
            gisWebsite.textContent = 'GIS Website';
            cadWebsite.textContent = 'CAD Website';
            planningDepartmentContact.textContent = 'Planning Department Contact';
            recorderClerkContact.textContent = 'Reorder Clerk Contact';
            taxOfficeContact.textContent = 'Tax Office Contact';
            assessorsOfficeContact.textContent = 'Assessors Office Contact';
            backTaxes.textContent = 'Back Taxes';
            taxLiens.textContent = 'Tax Liens';
            annualPropertyTaxes.textContent = 'Annual Property Taxes';
            isPropertyPartOfAnHoa.textContent = 'Is Property Part Of An Hoa';
            howMuchDues.textContent = 'Is so how much are the dues?';
            zoning.textContent = 'Zoning';
            terrianType.textContent = 'Terrian Type';
            propertyUseCode.textContent = 'Property Use Code';
            whatCanBeBuilt.textContent = 'What can be build on the Property';
            timeLimitToBuild.textContent = 'Time Limit to Build';
            canCamp.textContent = 'Can you camp on the property';
            notesOnCamping.textContent = 'Notes On Camping';
            rvAllowed.textContent = 'RV Allowed';
            noteOnRv.textContent = 'Notes On RV';
            mobileHomes.textContent = 'Mobile Homes';
            notesOnMobileHomes.textContent = 'Notes on Mobile Homes';
            isPropertyFloodZoneArea.textContent = 'Is the property in the flood zone area';
            water.textContent = 'Water';
            sewerOrSeptic.textContent = 'Sewer Or Septic';
            power.textContent = 'Power';
            gas.textContent = 'Gas';
            waste.textContent = 'Waste';
            dateCompleted.textContent = 'Date Completed';
            notesFromTheClient.textContent = 'Notes From the Client';
            notesFromTheQualitySpecialist.textContent = 'Notes From the Quality Specialist';
            notesFromTheVirtualAssistant.textContent = 'Notes From the Virtual Assistant';
            notesOnUtilities.textContent = 'Notes on Utilities';
            notesOnTax.textContent = 'Notes on Tax';
            notesOnLegalDescription.textContent = 'Notes on Legal Description';
            notesOnDeeds.textContent = 'Notes on Deeds';
            ddVaAssignedInitialData.textContent = 'VA assigned for gathering initial data';
            ddVaAssignedCallsOutsTaxData.textContent = 'VA Assigned for call outs for Tax data';
            ddVaAssignedCallsOutsZoningData.textContent = 'VA Assigned for call outs on Zoning data';
            ddVaAssignedCallsOutsUtilitiesData.textContent = 'VA Assigned for call outs on Utilities data';
            ddVaAssignedCallsOutsOtherRequest.textContent = 'VA Assigned for call outs on Other Requests';
            projectManager.textContent = 'Project Manager';
            statusOfDd.textContent = 'Status of DD';
            initialDueDiligenceCompletion.textContent = 'Date of Completion – Initial Data';
            taxDataCompletion.textContent = 'Date of Completion – Tax Data';
            zoningDataCompletion.textContent = 'Date of Completion – Zoning Data';
            utilitiesDataCompletion.textContent = 'Date of Completion – Utilities Data';
            otherRequestsCompletion.textContent = 'Date of Completion – Other Requests';
            dateOfCompletion.textContent = 'Date of Completion Submitted to the Client- Overall Due Diligence';
            operatorDetailsTaxData.textContent = 'County Operator Details - Tax Data';
            operatorDetailsZoningData.textContent = 'County Operator Details - Zoning Data';
            operatorDetailsUtilitiesData.textContent = 'County Operator Details - Utilities Data';
            operatorDetailsOtherRequests.textContent = 'County Operator Details - Other Requests';
            statusInitialData.textContent = 'Due Diligence Status for Initial Data';
            statusTaxData.textContent = 'Due Diligence Status for Tax Data';
            statusZoningData.textContent = 'Due Diligence Status for Zoning Data';
            statusUtilitiesData.textContent = 'Due Diligence Status for Utilities Data';
            statusOtherRequests.textContent = 'Due Diligence Status for Other Requests';
            levelOfUrgency.textContent = 'Level of Urgency';

            tr.appendChild(dateRequested);
            tr.appendChild(companyName);
            tr.appendChild(companyOwnerOrRequestor);
            tr.appendChild(dueDate);
            tr.appendChild(customerCare);
            tr.appendChild(ownerName);
            tr.appendChild(parcelNumber);
            tr.appendChild(accountNumber);
            tr.appendChild(propertyAddress);
            tr.appendChild(county);
            tr.appendChild(lotNumber);
            tr.appendChild(legalDescription);
            tr.appendChild(parcelSize);
            tr.appendChild(gpsCoordinates);
            tr.appendChild(gpsCoordinates4Corners);
            tr.appendChild(googleMapLink);
            tr.appendChild(elevation);
            tr.appendChild(assessedValue);
            tr.appendChild(accessToProperty);
            tr.appendChild(closestMajorCity);
            tr.appendChild(closestSmallTown);
            tr.appendChild(nearbyAttractions);
            tr.appendChild(assessorWebsite);
            tr.appendChild(treasurerWebsite);
            tr.appendChild(reorderClerkWebsite);
            tr.appendChild(zoningDepartmentWebsite);
            tr.appendChild(gisWebsite);
            tr.appendChild(cadWebsite);
            tr.appendChild(planningDepartmentContact);
            tr.appendChild(recorderClerkContact);
            tr.appendChild(taxOfficeContact);
            tr.appendChild(assessorsOfficeContact);
            tr.appendChild(backTaxes);
            tr.appendChild(taxLiens);
            tr.appendChild(annualPropertyTaxes);
            tr.appendChild(isPropertyPartOfAnHoa);
            tr.appendChild(howMuchDues);
            tr.appendChild(zoning);
            tr.appendChild(terrianType);
            tr.appendChild(propertyUseCode);
            tr.appendChild(whatCanBeBuilt);
            tr.appendChild(timeLimitToBuild);
            tr.appendChild(canCamp);
            tr.appendChild(notesOnCamping);
            tr.appendChild(rvAllowed);
            tr.appendChild(noteOnRv);
            tr.appendChild(mobileHomes);
            tr.appendChild(notesOnMobileHomes);
            tr.appendChild(isPropertyFloodZoneArea);
            tr.appendChild(water);
            tr.appendChild(sewerOrSeptic);
            tr.appendChild(power);
            tr.appendChild(gas);
            tr.appendChild(waste);
            tr.appendChild(dateCompleted);
            tr.appendChild(notesFromTheClient);
            tr.appendChild(notesFromTheQualitySpecialist);
            tr.appendChild(notesFromTheVirtualAssistant);
            tr.appendChild(notesOnUtilities);
            tr.appendChild(notesOnTax);
            tr.appendChild(notesOnLegalDescription);
            tr.appendChild(notesOnDeeds);
            tr.appendChild(ddVaAssignedInitialData);
            tr.appendChild(ddVaAssignedCallsOutsTaxData);
            tr.appendChild(ddVaAssignedCallsOutsZoningData);
            tr.appendChild(ddVaAssignedCallsOutsUtilitiesData);
            tr.appendChild(ddVaAssignedCallsOutsOtherRequest);
            tr.appendChild(projectManager);
            tr.appendChild(statusOfDd);
            tr.appendChild(initialDueDiligenceCompletion);
            tr.appendChild(taxDataCompletion);
            tr.appendChild(zoningDataCompletion);
            tr.appendChild(utilitiesDataCompletion);
            tr.appendChild(otherRequestsCompletion);
            tr.appendChild(dateOfCompletion);
            tr.appendChild(operatorDetailsTaxData);
            tr.appendChild(operatorDetailsZoningData);
            tr.appendChild(operatorDetailsUtilitiesData);
            tr.appendChild(operatorDetailsOtherRequests);
            tr.appendChild(statusInitialData);
            tr.appendChild(statusTaxData);
            tr.appendChild(statusZoningData);
            tr.appendChild(statusUtilitiesData);
            tr.appendChild(statusOtherRequests);
            tr.appendChild(levelOfUrgency);

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
            link.href = `/land-master/${id}/duediligence-report.pdf`;
            link.download = 'duediligence-Report-' + Date.now();
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
        sortedDueDiligence: function () {
            return this.dueDiligences.sort((a, b) => {
                let modifier = 1;
                if (this.currentSortDir === 'desc') modifier = -1;
                if (a[this.currentSort] < b[this.currentSort]) return -1 * modifier;
                if (a[this.currentSort] > b[this.currentSort]) return 1 * modifier;
                return 0;
            }).filter((row, index) => {
                let start = (this.currentPage - 1) * this.pageSize;
                let end = this.currentPage * this.pageSize;
                if (index >= start && index < end) return true;
            });
        }
    },
})