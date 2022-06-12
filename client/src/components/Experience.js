import { Button, TextField } from '@mui/material';
import moment from 'moment';
import React, { useState } from 'react';
import PrimaryButton from './PrimaryButton';
import { FormGroup } from '@mui/material';
import SecondaryButton from './SecondaryButton';

const defaultValues = {
  company_name: '',
  start_date: '',
  end_date: '',
  role_title: '',
};

function Experience({ experience }) {
  const [displayForm, setDisplayForm] = useState(false);
  const [formValues, setFormValues] = useState(defaultValues);
  const getYears = (from, to) => {
    let startDate = moment(from).get('year');
    let endDate = moment(to).get('year');

    return endDate - startDate;
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormValues({
      ...formValues,
      [name]: value,
    });
  };


  const handleSubmit = (event) => {
    event.preventDefault();
    setDisplayForm(false);
    console.log(formValues);
  };
  

  return (
    <>
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
          marginBottom: '20px',
        }}
      >
        {experience.map((experience) => (
          <div
            style={{
              display: 'flex',
              flexDirection: 'row',
              justifyContent: 'space-between',
            }}
          >
            <div
              style={{
                display: 'flex',
                flexDirection: 'column',
              }}
            >
              <p>
                {experience.role_title}
                <br />
                <span style={{ color: '#9F9F9F' }}>
                  {experience.company_name}
                </span>
              </p>
            </div>

            <div>
              <p style={{ color: '#9F9F9F' }}>
                {getYears(experience.start_date, experience.end_date)} years
              </p>
            </div>
          </div>
        ))}
        {displayForm && (
          <form
            onSubmit={handleSubmit}
            style={{
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'space-between',
              alignItems: 'space-between',
              marginBottom: '20px',
            }}
          >
            <label>Company Name</label>
            <TextField
              name="company_name"
              id="outlined-basic"
              variant="outlined"
              value={formValues.company_name}
              onChange={handleInputChange}
            />
            <label>Start Date</label>
            <TextField
              name="start_date"
              id="outlined-basic"
              variant="outlined"
              type="date"
              value={formValues.start_date}
              onChange={handleInputChange}
            />
            <label>End Date</label>
            <TextField
              name="end_date"
              id="outlined-basic"
              variant="outlined"
              type="date"
              value={formValues.end_date}
              onChange={handleInputChange}
            />
            <label>Position</label>
            <TextField
              name="role_title"
              id="outlined-basic"
              variant="outlined"
              value={formValues.role_title}
              onChange={handleInputChange}
            />
            <SecondaryButton
              variant="contained"
              type={'submit'}
              text={'Submit'}
            ></SecondaryButton>
          </form>
        )}
      </div>
      <PrimaryButton
        onClick={() => setDisplayForm(true)}
        text={'Add work experience'}
      />
    </>
  );
}

export default Experience;
