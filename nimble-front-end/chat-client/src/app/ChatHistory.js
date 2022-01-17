import React, { useState, useEffect, Fragment } from 'react';

const ChatHistory = () => {
  const [messages, setMessages] = useState('');

  useEffect(() => {
    if (localStorage.getItem('token') === null) {
      console.log("Cant get token");
      window.location.replace('http://localhost:3000/login');
    } else {
      fetch('http://127.0.0.1:8000/api/v1/users/messages', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Token ${localStorage.getItem('token')}`
        }
      })
        .then(res => res.json())
        .then(data => {
          console.log(data.messages);

          setMessages(data.messages);
        });
    }
  }, []);

  return (
    <div>
      {(
        <Fragment>
          <div className="messages"> { messages && messages.map(
            (message, index) => {
              return(
                <div className="Message" key={index}>
                <p> {message.content}</p>
              </div>
                );
            })} 
          </div>
        </Fragment>
      )}
    </div>
  );
};

export default ChatHistory;