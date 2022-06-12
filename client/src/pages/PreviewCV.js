import { Stack } from '@mui/material';
import React from 'react';
import AboutMe from '../components/AboutMe';

import Experience from '../components/Experience';
import PrimaryButton from '../components/PrimaryButton';
import SecondaryButton from '../components/SecondaryButton';
import Skills from '../components/Skills';
import DATA from '../userData';

function PreviewCV() {
  return (
    <Stack>
      <AboutMe aboutMe={DATA.about_me.about_me_text} />

      <h1>Work Experience</h1>
      <Experience experience={DATA.work_experience} />
      <h1>Skills</h1>
      <Skills skills={DATA.skills} />

      <SecondaryButton type={'submit'} text={'Submit your CV'} />
    </Stack>
  );
}

export default PreviewCV;
