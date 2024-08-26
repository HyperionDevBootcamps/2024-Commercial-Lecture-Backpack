import React, { useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

const Profile = () => {
  const { user } = useContext(AuthContext);

  return (
    <div className="profile">
      <h2>Profile Page</h2>
      {user ? (
        <div>
          <p>Username: {user.name}</p>
          <p>Email: user@example.com (Sample)</p>
        </div>
      ) : (
        <p>Please log in to view your profile information.</p>
      )}
    </div>
  );
};

export default Profile;