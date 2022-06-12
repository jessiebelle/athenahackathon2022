import { Stack, TextField } from '@mui/material';
import React, { useState } from 'react';
import PrimaryButton from './PrimaryButton';
import SecondaryButton from './SecondaryButton';

export default function Skills({ skills }) {
  const defaultValues = {
    skill: '',
  };
  const [displayForm, setDisplayForm] = useState(false);
  const [formValues, setFormValues] = useState(defaultValues);

  const deleteSkill = () => {
    console.log('deleteSkill');
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormValues({
      ...formValues,
      [name]: value,
    });
  };

  const addSkill = (event) => {
    event.preventDefault();
    setDisplayForm(false);
    console.log('submit this skill:');
  };

  return (
    <Stack>
      <div
        style={{
          display: 'flex',
          flexDirection: 'row',
          flexWrap: 'wrap',
          marginBottom: '10px',
        }}
      >
        {skills &&
          skills.map((skill) => (
            <div
              style={{
                margin: '5px',
                background: '#DBDBDB',
                width: 'fit-content',
                padding: '4px',
                alignItems: 'center',
                borderRadius: '4px',
              }}
            >
              {skill.skill_name_by_language[0].skill_display_name}
              <span style={{ margin: '5px' }} onClick={deleteSkill}>
                X
              </span>
            </div>
          ))}
      </div>
      {displayForm && (
        <form
          onSubmit={addSkill}
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignSelf: 'center',
            marginBottom: '20px',
            width: '50%',
          }}
        >
          <TextField
            name="skill"
            id="outlined-basic"
            variant="outlined"
            size="small"
            onChange={handleInputChange}
            value={formValues.skill}
          />
          <SecondaryButton
            variant="contained"
            type={"submit"}
            text={'submit'}
          ></SecondaryButton>
        </form>
      )}
      <PrimaryButton onClick={() => setDisplayForm(true)} text={'Add Skill'} />
    </Stack>
  );
}
