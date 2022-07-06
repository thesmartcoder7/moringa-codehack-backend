import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create-test',
  templateUrl: './create-test.component.html',
  styleUrls: ['./create-test.component.css']
})
export class CreateTestComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    let sendInvite = document.querySelector("#sendinvite") as HTMLDivElement;
    let inviteCheckbox = document.querySelector("#sendinvitecheckbox") as HTMLInputElement

    inviteCheckbox.addEventListener('change', function() {
      if (this.checked) {
        sendInvite.style.display='block'
      } else {
        sendInvite.style.display='none'
      }
    });
  }

}
