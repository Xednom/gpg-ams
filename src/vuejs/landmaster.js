Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-land-master',
    delimiters: ['[[',']]'],
    data: {
        loading: false,
        clientNames: [],
        newDueDiligence: {
            'date_requested': '',
            'company_name': '',
            'company_owner': '',
            'date_completed_or_returned': '',
        },
        newLandData: {
            'owner_name': '',
            'parcel_number': '',
            'account_number': '',
            'property_address': '',
            'county': '',
            'lot_number': '',
            'legal_description': '',
            'parcel_size': '',
            'gps_coordinates': '',
            'gps_coordinates_4_corners': '',
            'google_map_link': '',
            'elevation': '',
            'assessed_value': '',
            'access_to_property': '',
        },
        newAdditionalLandInfo: {
            'client_name': '',
            'closest_major_city': '',
            'closest_small_town': '',
            'nearby_attractions': '',
        },
        newCountyData: {
            'client_name': '',
            'assessor_website': '',
            'treasurer_website': '',
            'recorder_cleark_website': '',
            'zoning_department_website': '',
            'gis_website': '',
            'cad_website': '',
            'planning_department_contact': '',
            'recorder_clerk_contact': '',
            'tax_office_contact': '',
            'assessors_office_contact': '',
        },
        newTaxData: {
            'client_name': '',
            'back_taxes': '',
            'tax_liens': '',
            'annual_property_taxes': '',
            'is_property_part_of_an_hoa': '',
            'how_much_dues': '',
        },
        newZoningData: {
            'client_name': '',
            'zoning': '',
            'terrian_type': '',
            'property_use_code': '',
            'what_can_be_built': '',
            'time_limit_to_build': '',
            'can_camp': '',
            'notes_on_camping': '',
            'rv_allowed': '',
            'note_on_rv': '',
            'mobile_homes': '',
            'notes_on_mobile_homes': '',
            'is_property_flood_zone_area': '',
        },
        newDataOnUtilities: {
            'client_name': '',
            'water': '',
            'sewer_or_septice': '',
            'power': '',
            'gas': '',
            'waste': '',
        },
    },
    mounted: function () {
        this.getClientNames();
    },
    methods: {
        resetDueDiligenceFields: function () {
            Object.keys(this.newDueDiligence).forEach(key => {
                this.newDueDiligence[key] = ''
            })
        },
        resetLandDataFields: function () {
            Object.keys(this.newLandData).forEach(key => {
                this.newLandData[key] = ''
            })
        },
        resetAdditionalLandInfoFields: function () {
            Object.keys(this.newAdditionalLandInfo).forEach(key => {
                this.newAdditionalLandInfo[key] = ''
            })
        },
        resetCountyDataFields: function () {
            Object.keys(this.newCountyData).forEach(key =>{
                this.newCountyData[key] = ''
            })
        },
        resetTaxDataFields: function () {
            Object.keys(this.newTaxData).forEach(key => {
                this.newTaxData[key] = ''
            })
        },
        resetZoningDataFields: function () {
            Object.keys(this.newZoningData).forEach(key => {
                this.newZoningData[key] = ''
            })
        },
        resetDataOnUtilitiesFields: function () {
            Object.keys(this.newDataOnUtilities).forEach(key => {
                this.newDataOnUtilities[key] = ''
            })
        },
        addAllApps: function () {
            this.addDueDiligence();
            this.addLandData();
            this.addAdditionalLandInfo();
            this.addCountyData();
            this.addTaxData();
            this.addZoningData();
            this.addDataOnUtilities();
        },
        getClientNames: function() {
            this.loading = true;
            this.$http.get(`/api/v1/due-diligence/`)
                .then((response) => {
                    this.clientNames = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addDueDiligence: function () {
            this.loading = true;
            this.$http.post('/api/v1/due-diligence/', this.newDueDiligence)
                .then((response) => {
                    this.loading = false;
                    this.resetDueDiligenceFields();
                    swal({
                        title: "GPG System",
                        text: "Due Diligence task has been added successfully!",
                        icon: "success",
                        buttons: false,
                        timer: 3000
                    })
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addLandData: function () {
            this.loading = true;
            this.$http.post('/api/v1/land-data/', this.newLandData)
                .then((response) => {
                    this.loading = false;
                    this.resetLandDataFields();
                })
                .catch((err) =>{
                    this.loading = false;
                    console.log(err);
                })
        },
        addAdditionalLandInfo: function () {
            this.loading = true;
            this.$http.post('/api/v1/additional-land-info/', this.newAdditionalLandInfo)
                .then((response) => {
                    this.loading = false;
                    this.resetAdditionalLandInfoFields();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addCountyData: function () {
            this.loading = true;
            this.$http.post('/api/v1/county-data/', this.newCountyData)
                .then((response) => {
                    this.loading = false;
                    this.resetCountyDataFields();
                })
                .catch((err) =>{
                    this.loading = false;
                    console.log(err);
                })
        },
        addTaxData: function () {
            this.loading = true;
            this.$http.post('/api/v1/tax-data/', this.newTaxData)
                .then((response) => {
                    this.loading = false;
                    this.resetTaxDataFields();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addZoningData: function () {
            this.loading = true;
            this.$http.post('/api/v1/zoning-data/', this.newZoningData)
                .then((response) => {
                    this.loading = false;
                    this.resetZoningDataFields();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        addDataOnUtilities: function () {
            this.loading = true;
            this.$http.post('/api/v1/data-on-utilities/', this.newDataOnUtilities)
                .then((response) => {
                    this.loading = false;
                    this.resetDataOnUtilitiesFields();
                })
                .catch((err) =>{
                    this.loading =false;
                    console.log(err);
                })
        },
    }
})