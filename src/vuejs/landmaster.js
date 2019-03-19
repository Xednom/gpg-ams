Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#gpg-land-master',
    delimiters: ['[[',']]'],
    data: {
        loading: false,
        clientNames: [],
        newDueDiligence: {
            'date_requested': null,
            'company_name': "",
            'company_owner': "",
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
            'sewer_or_septice': "",
            'power': "",
            'gas': "",
            'waste': "",
            'date_completed': null,
            'notes_from_the_client': "",
            'notes_from_the_land_master_team': "",
        },
    },
    mounted: function () {
        this.getClientNames();
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
        addDueDiligence: function () {
            this.loading = true;
            this.$http.post('/api/v1/due-diligence/', this.newDueDiligence)
                .then((response) => {
                    this.loading = false;
                    swal({
                        title: "GPG System",
                        text: "Due Diligence task has been added successfully!",
                        icon: "success",
                        buttons: false,
                        timer: 3000
                    })
                    this.resetDueDiligenceFields();
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
    }
})