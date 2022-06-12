import React, { useState } from 'react';

function SkillItem({ skill }) {
  const [hide, setHide] = useState(false);
  const deleteSkill = () => {
    setHide(true);
    console.log('deleteSkill');
  };
  return (
    <div
      hidden={hide}
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
  );
}

export default SkillItem;
