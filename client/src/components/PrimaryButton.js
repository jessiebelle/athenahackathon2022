import { Button } from '@mui/material';

import React from 'react';

export default function PrimaryButton({ text, onClick }) {
  return (
    <Button
      variant="contained"
      style={{
        textTransform: 'none',
        background: '#DFB2F4',
        color: '#7A39C2',
        fontWeight: '600',
        width: 'fit-content',
        justifyContent: 'center',
        alignSelf: 'center',
        display: 'flex',
      }}
      onClick={onClick}
    >
      {text}
    </Button>
  );
}
