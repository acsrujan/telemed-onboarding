from onboarding.models import Doctor


def write_csv_file(writer, doctor_onboarding_status):
    fields = ['id', 'mci', 'state_authority', 'organisation_name', 'onboarding_status']

    # write the headers
    writer.writerow(fields)

    # Get all the doctors for the status
    doctors = Doctor.objects.filter(onboarding_status=doctor_onboarding_status, doctor_data_already_downloaded=False)

    # get data from database.
    for doctor in doctors:
        row_data = list()
        for field in fields:
            row_data.append(getattr(doctor, field))

        writer.writerow(row_data)

    doctors.update(doctor_data_already_downloaded=True)
