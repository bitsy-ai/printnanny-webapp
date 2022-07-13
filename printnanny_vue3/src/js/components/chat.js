/**
 * Theme: Hyper - Responsive Bootstrap 5 Admin Dashboard
 * Author: Coderthemes
 * Module/App: CRMDashboard
 */

import moment from 'moment';

class Chat {

  constructor() {
    this.chatInput = document.querySelector('.chat-input');
    this.chatList = document.querySelector('.conversation-list');
    this.chatSendBtn = document.querySelector('.chat-send');
    this.chatForm = document.getElementById('chat-form');
  }

  save() {
    const chatText = this.chatInput.value;
    const chatTime = moment()
      .format('h:mm');
    if (chatText === "") {
      this.chatInput.focus();
      return false;
    } else {
      this.chatList.innerHTML += '<li class="clearfix odd"><div class="chat-avatar"><img src="/images/users/avatar-1.jpg" alt="male"><i>' + chatTime + '</i></div><div class="conversation-text"><div class="ctext-wrap"><i>Dominic</i><p>' + chatText + '</p></div></div></li>';
      this.chatInput.focus();
      this.chatInput.scrollTop = this.chatInput.scrollHeight;
      //TODO:... Scroll is not working
      this.chatList.animate({ scrollTop: this.chatList.scrollHeight }, 1000);
      return true;
    }
  }


  init() {

    const self = this;

    if (this.chatForm) {
      this.chatForm.addEventListener('submit', function (ev) {
        ev.preventDefault();
        self.save();
        self.chatForm.classList.remove('was-validated');
        self.chatInput.value = "";
        return false;
      });
    }

  }

}

export default Chat;
