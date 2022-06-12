const DATA = {
  user_id: 1,
  user_details: {
    name: 'Tom',
    phone_number: '09876543235',
    email: 'mg@gmail.com',
    date_of_birth: '1980-01-01',
    languages: {
      primary_language: 'English',
      secondary_languages: ['Kurdish', 'Hungarian'],
    },
  },
  work_experience: [
    {
      company_id: 1,
      company_name: 'Beamery',
      start_date: '2020-01-01',
      end_date: '2021-01-01',
      role_title: 'Software Developer',
      details: {
        details_text:
          'Details Details Details Details Details Details Details Details',
        language_id: 'en',
      },
    },
    {
      company_id: 2,
      company_name: 'Deliveroo',
      start_date: '2015-01-01',
      end_date: '2020-01-01',
      role_title: 'Software Developer',
      details: {
        details_text:
          'Details Details Details Details Details Details Details Details',
        language_id: 'en',
      },
    },
  ],
  skills: [
    {
      skill_id: 1,
      skill_name_by_language: [
        {
          skill_display_name: 'Python',
          language_id: 'en',
        },
      ],
    },
    {
      skill_id: 2,
      skill_name_by_language: [
        {
          skill_display_name: 'Java',
          language_id: 'en',
        },
      ],
    },
    {
      skill_id: 3,
      skill_name_by_language: [
        {
          skill_display_name: 'JavaScript',
          language_id: 'en',
        },
      ],
    },
    {
      skill_id: 4,
      skill_name_by_language: [
        {
          skill_display_name: 'Agile',
          language_id: 'en',
        },
      ],
    },
    {
      skill_id: 5,
      skill_name_by_language: [
        {
          skill_display_name: 'Team Leading',
          language_id: 'en',
        },
      ],
    },
  ],
  about_me: {
    about_me_text:
      "I am a career expert and Certified Professional Resume Writer who has published over 200 in-depth articles on Zety. Since 2016, he has been sharing advice on all things recruitment from writing winning resumes and cover letters to getting a promotion.",
    language_id: 'en',
  },
};

export default DATA;
