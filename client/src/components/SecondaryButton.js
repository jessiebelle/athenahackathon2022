import { Button } from '@mui/material';

import React from 'react';

export default function SecondaryButton({ text, onClick, type }) {
  return (
    <Button
      variant="contained"
      style={{
        textTransform: 'none',
        marginTop: '20px',
        marginBottom: '20px',
        background: '#5407DC',
        color: '#DFB2F4',
        fontWeight: '600',
        width: 'fit-content',
        justifyContent: 'center',
        alignSelf: 'center',
        display: 'flex',
      }}
      onClick={onClick}
      type={type}
    >
      {text}
    </Button>
  );
}
