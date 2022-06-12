import { TextareaAutosize, TextField } from '@mui/material';
import React, { useState } from 'react';
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
  const editAboutMe = (event) => {
    event.preventDefault();
    setDisplayForm(false);
    console.log(formValues);
  };

  return (
    <>
      <h1> About Me </h1>
      {displayForm ? (
        <form
          onSubmit={editAboutMe}
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
            name="skill"
            id="outlined-basic"
            variant="outlined"
            type="text"
            style={{ width: 300 }}
            inputMode="text"
            defaultValue={formValues.aboutMe}
            onInput={handleInputChange}
          />
          <SecondaryButton
            variant="contained"
            type={'submit'}
            text={'Submit'}
          ></SecondaryButton>
        </form>
      ) : (
        <>
          <p> {aboutMe}</p>
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
