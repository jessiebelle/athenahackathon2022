import { TextareaAutosize, TextField } from '@mui/material';
import React, { useState, useEffect } from 'react';
import PrimaryButton from './PrimaryButton';
import SecondaryButton from './SecondaryButton';

function AboutMe({ aboutMe }) {
  const defaultValues = {
    aboutMe: aboutMe,
  };
  const [displayForm, setDisplayForm] = useState(false);
  const [formValues, setFormValues] = useState(defaultValues);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormValues({
      ...formValues,
      [name]: value,
    });
  };

  useEffect(() => {
    console.log('change');
  }, [formValues]);

  const handleSubmit = (event) => {
    // Here we would also post update to our endpoint once we have it!
    event.preventDefault();
    const { name, value } = event.target;
    setFormValues({
      ...formValues,
      [name]: value,
    });
    setDisplayForm(false);
    console.log(formValues);
    console.log('sub');
  };

  return (
    <>
      <h1> About Me </h1>
      {displayForm ? (
        <form
          onSubmit={handleSubmit}
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignSelf: 'center',
            alignItems: 'center',
            marginBottom: '20px',
            width: '50%',
          }}
        >
          <TextareaAutosize
            name="aboutMe"
            id="outlined-basic"
            variant="outlined"
            type="text"
            style={{ width: 300 }}
            inputMode="text"
            defaultValue={formValues.aboutMe}
            onChange={handleInputChange}
          />
          <SecondaryButton
            variant="contained"
            type={'submit'}
            text={'Submit'}
          ></SecondaryButton>
        </form>
      ) : (
        <>
          <p> {formValues.aboutMe}</p>
          <PrimaryButton
            onClick={() => setDisplayForm(true)}
            text={'Edit about me'}
          />
        </>
      )}
    </>
  );
}

export default AboutMe;
