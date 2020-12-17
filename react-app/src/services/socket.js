import io from "socket.io-client";
import { baseUrl } from "../config";

export function getDraftSocket() {
  const socket = io.connect(baseUrl);

  socket.on('connect', () => {
    console.log('I connected', socket.id);
    socket.emit('I\'m connected!');
  });

  socket.on('disconnect', (reason) => {
    console.log('I disconnected', reason);
  });

  socket.on('error', (error) => {
    console.log('Error');
    console.error(error);
  });

  socket.on('connect_error', (error) => {
    console.log('Connect Error');
    console.error(error);
  });

  socket.on('join_draft', function (msg) {
    console.log(msg);
  });

  return socket;
}

