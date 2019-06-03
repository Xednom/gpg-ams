from django.contrib import admin

from .models import (
    CygnusInvestmentSeller,
    DreamWeaverProperty,
    OfficeFlowersValleyProperties,
    SolidWorkProperties,
    NewLeafInvestors,
    LibertyLands,
    LynkCapital,
    DreamCloudBuyLand,
    LandQuestPro,
    LandRapid,
    Alevi,
    AffordaleLandInvestment,
    AffordableLandSpiels,
    LGPropertyVentures,
    FranklinManagement,
)


class CygnusInvestmentProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'name', 'property_owner',
                    'other_owners', 'email_address', 'average_handling_time')
    list_filter = ('customer_care_specialist',)
    search_fields = ('customer_care_specialist', 'email_address', 'name')
    fieldsets = (
        ("Seller Information for Cygnus Investment", {
            'fields': (
                'customer_care_specialist',
                'provided_contact_information',
                'number_printed',
                'name',
                'property_owner',
                'other_owners',
                'phone_number',
                'email_address',
                'average_handling_time',
                'additional_notes'
            )
        }),
        ("Date Information", {
            'fields': (
                'call_date',
            )
        }),
    )


class DreamWeaverPropertyProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'name',
                    'reference_number_or_parcel_number', 'email_address', 'state_and_county',
                    'owner_of_the_land')
    list_filter = ('customer_care_specialist',)
    search_fields = ('customer_care_specialist', 'email_address', 'reference_number_or_parcel_number')
    fieldsets = (
        ("Seller Information for Dream Weaver Property", {
            'fields': (
                'customer_care_specialist',
                'name',
                'reference_number_or_parcel_number',
                'state_and_county',
                'owner_of_the_land',
                'price',
                'price_to_sell',
                'phone_number',
                'email_address',
                'average_handling_time',
                'additional_notes',
            )
        }),
        ("Date Information", {
            'fields': (
                'call_date',
            )
        }),
    )


class OfficeFlowersVallerPropertiesProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'name', 
                    'phone_number', 'interested_in_selling', 'land_or_house',
                    'co_owners', 'owner')
    list_filter = ('customer_care_specialist',)
    fieldsets = (
        ("Seller Information for Dream Weaver Property", {
            'fields': (
                'customer_care_specialist',
                'name',
                'phone_number',
                'interested_in_selling',
                'land_or_house',
                'id_number',
                'co_owners',
                'owner',
                'good_phone_number',
                'verify_the_information',
                'property_to_sell',
                'size_of_the_property',
                'hoa_in_this_area',
                'own_the_property_free_and_clear',
                'improvements',
                'electricity',
                'road_access',
                'owned_the_property',
                'pay_cash_and_close',
                'property_currently_listed',
                'name_and_phone_number_of_agent',
                
            )
        }),
        ("Spiel", {
            'fields': (
                'opening_spiel',
                'closing_spiel',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'date_listed',
                'average_handling_time',
            )
        }),
        ("Other Informations", {
            'fields': (
                'additional_comments',
                'additional_notes',
            )
        }),
    )


class SolidWorkPropertiesProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'name',
                    'lot_apn_number', 'property_owner', 'other_owners', 'phone_number',)
    list_filter = ('customer_care_specialist', 'name', 'lot_apn_number')
    search_fields = ('customer_care_specialist', 'name', 'lot_apn_number')
    fieldsets = (
        ("Seller Information for Solid Work Properties Seller", {
            'fields': (
                'customer_care_specialist',
                'name',
                'lot_apn_number',
                'property_owner',
                'other_owners',
                'phone_number',
                'mailing_address',
                'structure',
                'perc_test',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
            )
        }),
    )


class NewLeafInvestorsProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'name', 'phone_number',
                    'owner_of_record', 'email_address', 'city', 'state')
    list_filter = ('customer_care_specialist', 'name', 'city', 'state')
    search_fields = ('customer_care_specialist', 'name', 'state_and_county')
    fieldsets = (
        ("Seller Information for New Leaf Investors", {
            'fields': (
                'customer_care_specialist',
                'name',
                'phone_number',
                'receive_a_letter_or_voicemail',
                'owner_of_record',
                'phone_number_to_reach',
                'email_address',
                'mailing_address',
                'mailing_address_2',
                'city',
                'state',
                'zip_code',
                'apn',
                'own_the_property',
                'property_listed',
                'state_and_county',
            )
        }),
        ("Spiel", {
            'fields': (
                'opening_spiel',
                'closing_spiel',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
            )
        }),
    )


class LibertyLandsProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'reference_number',
                    'name', 'property_owner', 'other_owners', 'phone_number')
    list_filter = ('customer_care_specialist', 'name', 'call_date')
    search_fields = ('customer_care_specialist', 'name', 'apn', 'owner_of_record')
    fieldsets = (
        ("Seller Information for Liberty Lands", {
            'fields': (
                'customer_care_specialist',
                'name',
                'phone_number',
                'receive_a_letter_or_voicemail',
                'owner_of_record',
                'phone_number_to_reach',
                'email_address',
                'mailing_address',
                'mailing_address_2',
                'city',
                'state',
                'zip_code',
                'apn',
                'own_the_property',
                'property_listed',
                'state_and_county',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
            )
        }),
    )


class LynkCapitalProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'name', 'phone_number',
                    'city', 'state', 'zip_code', 'county', 'apn_number')
    list_filter = ('customer_care_specialist', 'name', 'city', 'state')
    search_fields = ('customer_care_specialist', 'name', 'city', 'state', 'name_on_the_letter',
                     'apn_number')
    fieldsets = (
        ("Seller Information for Lynk Capital", {
            'fields': (
                'customer_care_specialist',
                'name',
                'phone_number',
                'offer_on_property',
                'property_address',
                'city',
                'state',
                'zip_code',
                'county',
                'letter',
                'apn_number',
                'name_on_the_letter',
                'water_connections',
                'electricity',
                'access_to_property',
                'paved_or_dirt',
                'structure_on_property',
                'property_listed_on_realtor',
                'property_been_flooded',
                'property_cleared_or_wooded',
                'cleared',
                'owned_the_property',
                'purchase_acquire_the_property',
                'inherited_from',
                'currently_listed',
                'if_not_then_who',
                'hoa',
                'property_taxes',
                'if_not_current',
                'liens',
                'mobile_homes_allowed',
                'original_plans',
                'interested_in_selling',
                'asking_price',
                'if_yes_how_much',
                'best_day_time_to_call',
                'best_number_to_call',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Spiel", {
            'fields': (
                'opening_spiel',
                'received_a_letter_spiel',
                'before_spiel',
                'closing_spiel',
            )
        }),
        ("Frequently Asked Questions", {
            'fields': (
                'faq',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
            )
        }),
    )


class DreamCloudBuyLandProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'name', 'phone_number',
                    'owner_of_record')
    list_filter = ('customer_care_specialist', 'name', 'owner_of_record')
    search_fields = ('customer_care_specialist', 'name', 'owner_of_record')
    fieldsets = (
        ("Seller Information for Dream Cloud Buy Land", {
            'fields': (
                'customer_care_specialist',
                'name',
                'phone_number',
                'interested_in_selling',
                'number_at_the_bottom_right',
                'best_address',
                'owner_of_record',
                'additional_owners',
                'own_the_property_free_and_clear',
                'other_information',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
                'additional_notes_from_csr',
            )
        }),
    )


class LandQuestProProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'caller_name', 'phone_number',
                    'other_owners', 'reference_number')
    list_filter = ('customer_care_specialist', 'caller_name', 'other_owners')
    search_fields = ('customer_care_specialist', 'caller_name', 'other_owners', 'phone_number')
    fieldsets = (
        ("Seller Information for Land Quest Pro", {
            'fields': (
                'customer_care_specialist',
                'name',
                'phone_number',
                'caller_name',
                'other_owners',
                'reference_number',
                'prefer_to_contact',
                'other_details',
                'other_properties',
                'last_questions',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
            )
        }),
    )


class LandRapidProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'caller_name', 'phone_number',
                    'email_address', 'owner_name', 'other_co_owners')
    list_filter = ('customer_care_specialist', 'caller_name',
                   'owner_name', 'other_co_owners')
    search_fields = ('customer_care_specialist', 'caller_name',
                     'owner_name', 'other_co_owners')
    fieldsets = (
        ("Seller Information for Land Rapid Pro", {
            'fields': (
                'customer_care_specialist',
                'name',
                'caller_name',
                'phone_number',
                'email_address',
                'offer_price_listed',
                'owner_name',
                'relationship',
                'other_co_owners',
                'signers',
                'how_did_you_aquire_the_property',
                'when_did_you_aquire_the_property',
                'title_issues',
                'back_taxes_on_the_property',
                'selling_the_property',
                'state_property_located',
                'county_property_located',
                'city_property_located',
                'address_or_parcel_id',
                'size_and_dimensions',
                'road_access',
                'utilities',
                'other_improvements',
                'any_structures',
                'mortgages_or_liens',
                'hoa',
                'current_zoning',
                'currently_listed',
                'about_the_property',
                'own_any_other_properties',
                'should_note',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
            )
        }),
    )


class AleviProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'phone_number',
                    'owner_of_record', 'reference_number')
    list_filter = ('customer_care_specialist', 'owner_of_record', 'size')
    search_fields = ('customer_care_specialist', 'owner_of_record', 'reference_number'
                     'size')
    fieldsets = (
        ("Seller Information for Land Quest Pro", {
            'fields': (
                'customer_care_specialist',
                'phone_number',
                'reference_number',
                'owner_of_record',
                'interested_in_selling',
                'several_properties',
                'size',
                'road_access',
                'utilities',
                'improvements',
                'owned_the_property',
                'back_taxes',
                'owners_association',
                'listed_with_real_estate_agent',
                'last_question',
            )
        }),
        ("Spiel", {
            'fields': (
                'opening_spiel',
                'optional_comments',
                'closing_spiel',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
            )
        }),
    )


class AffordableLandInvestmentProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'contact_information',
                    'name', 'state_county', 'state_county', 'email_address')
    list_filter = ('customer_care_specialist', 'name',
                   'state_county', 'state_county', 'email_address')
    search_fields = ('call_date', 'customer_care_specialist', 'contact_information',
                     'name', 'state_county', 'state_county', 'email_address')
    fieldsets = (
        ("Seller Information for Affordable Land Investment", {
            'fields': (
                'customer_care_specialist',
                'contact_information',
                'name',
                'state_county',
                'parcel_number',
                'property_owner',
                'other_owners',
                'sell_the_property',
                'phone_number',
                'email_address',
                'listed_in_letter_or_postcard',
                'for_your_property',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
            )
        }),
    )


class AffordableLandSpielsProfile(admin.ModelAdmin):
    list_display = ('opening_spiel', 'closing_spiel')
    fieldsets = (
        ("Spiel Informations for Affordable Land Investments", {
            'fields': (
                'opening_spiel',
                'closing_spiel',
            )
        }),
    )


class LGPropertyVenturesProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist', 'reference_number',
                    'property_owner', 'access', 'selling_your_property', 'average_handling_time')
    list_filter = ('customer_care_specialist', 'property_owner')
    search_fields = ('customer_care_specialist', 'property_owner')
    fieldsets = (
        ("Seller Information for LG Property Ventures", {
            'fields': (
                'customer_care_specialist',
                'reference_number',
                'property_owner',
                'access',
                'selling_your_property',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
            )
        }),
    )


class FranklinManagementProfile(admin.ModelAdmin):
    list_display = ('call_date', 'customer_care_specialist',
                    'name', 'property_owner', 'other_owner',
                    'phone_number', 'email_address')
    list_filter = ('customer_care_specialist', 'name',
                   'property_owner', 'other_owner')
    search_fields = ('customer_care_specialist', 'name',
                     'property_owner', 'other_owner')
    fieldsets = (
        ("Seller Information for Franklin Management", {
            'fields': (
                'customer_care_specialist',
                'name',
                'property_owner',
                'other_owner',
                'phone_number',
                'email_address',
                'road_access',
                'property_currently_listed',
                'utilities',
                'consider_selling_it',
                'improvements',
                'hoa_poa',
                'back_taxes',
                'liens_in_property',
                'lowest_number',
                'closing_date',
                'other_properties',
                'know_about_the_property',
            )
        }),
        ("Spiel", {
            'fields': (
                'opening_spiel',
                'closing_spiel',
            )
        }),
        ("Date & Time Information", {
            'fields': (
                'call_date',
                'average_handling_time',
            )
        }),
        ("Other Information", {
            'fields': (
                'additional_notes',
            )
        }),
    )


admin.site.register(CygnusInvestmentSeller, CygnusInvestmentProfile)
admin.site.register(DreamWeaverProperty, DreamWeaverPropertyProfile)
admin.site.register(OfficeFlowersValleyProperties, OfficeFlowersVallerPropertiesProfile)
admin.site.register(SolidWorkProperties, SolidWorkPropertiesProfile)
admin.site.register(NewLeafInvestors, NewLeafInvestorsProfile)
admin.site.register(LibertyLands, LibertyLandsProfile)
admin.site.register(LynkCapital, LynkCapitalProfile)
admin.site.register(DreamCloudBuyLand, DreamCloudBuyLandProfile)
admin.site.register(LandQuestPro, LandQuestProProfile)
admin.site.register(LandRapid, LandRapidProfile)
admin.site.register(Alevi, AleviProfile)
admin.site.register(AffordaleLandInvestment, AffordableLandInvestmentProfile)
admin.site.register(AffordableLandSpiels, AffordableLandSpielsProfile)
admin.site.register(LGPropertyVentures, LGPropertyVenturesProfile)
admin.site.register(FranklinManagement, FranklinManagementProfile)

