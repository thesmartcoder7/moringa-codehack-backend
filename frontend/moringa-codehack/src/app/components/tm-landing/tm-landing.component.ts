import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-tm-landing',
  templateUrl: './tm-landing.component.html',
  styleUrls: ['./tm-landing.component.css']
})
export class TmLandingComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
    let titleWrapper=document.querySelector("#sidebar-nav") as HTMLUListElement
    let iconWrapper=document.querySelector("#sidebar-nav-icons") as HTMLUListElement
    let titleMenu=document.querySelector("#menu-toggle") as HTMLAnchorElement
    let iconMenu=document.querySelector("#menu-toggle-icons") as HTMLAnchorElement
    let navWrapper=document.querySelector("#sidebar-wrapper") as HTMLDivElement
    let pageWrapper=document.querySelector("#page-content-wrapper") as HTMLDivElement


    titleMenu.addEventListener('click', ()=>{
        iconWrapper.style.display='block'
        titleWrapper.style.display='none'
        navWrapper.style.width='7%'
        // pageWrapper.style.marginLeft='50%'
      
    })
    iconMenu.addEventListener('click', ()=>{
        titleWrapper.style.display='block'
        iconWrapper.style.display='none'
        navWrapper.style.width='15%'
        pageWrapper.style.paddingLeft='7%'
                    
    })



  

  }

}
