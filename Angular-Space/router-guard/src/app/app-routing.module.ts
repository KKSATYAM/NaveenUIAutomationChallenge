import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';
import { routerGuardGuard } from './router-guard.guard';
import { AccessDeniedComponent } from './access-denied/access-denied.component';

const routes: Routes = [

  {path:'home',component:HomeComponent},
  {path:'about',component:AboutComponent,canActivate:[routerGuardGuard]},
  {path:'contact',component:ContactComponent},
  {path: 'access-denied',component:AccessDeniedComponent}


];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
