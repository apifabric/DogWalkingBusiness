import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DogHomeComponent } from './home/Dog-home.component';
import { DogNewComponent } from './new/Dog-new.component';
import { DogDetailComponent } from './detail/Dog-detail.component';

const routes: Routes = [
  {path: '', component: DogHomeComponent},
  { path: 'new', component: DogNewComponent },
  { path: ':id', component: DogDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Dog-detail-permissions'
      }
    }
  },{
    path: ':dog_id/Booking', loadChildren: () => import('../Booking/Booking.module').then(m => m.BookingModule),
    data: {
        oPermission: {
            permissionId: 'Booking-detail-permissions'
        }
    }
},{
    path: ':dog_id/DogHistory', loadChildren: () => import('../DogHistory/DogHistory.module').then(m => m.DogHistoryModule),
    data: {
        oPermission: {
            permissionId: 'DogHistory-detail-permissions'
        }
    }
},{
    path: ':dog_id/Feedback', loadChildren: () => import('../Feedback/Feedback.module').then(m => m.FeedbackModule),
    data: {
        oPermission: {
            permissionId: 'Feedback-detail-permissions'
        }
    }
},{
    path: ':dog_id/MaintenanceLog', loadChildren: () => import('../MaintenanceLog/MaintenanceLog.module').then(m => m.MaintenanceLogModule),
    data: {
        oPermission: {
            permissionId: 'MaintenanceLog-detail-permissions'
        }
    }
},{
    path: ':dog_id/Service', loadChildren: () => import('../Service/Service.module').then(m => m.ServiceModule),
    data: {
        oPermission: {
            permissionId: 'Service-detail-permissions'
        }
    }
},{
    path: ':dog_id/Walk', loadChildren: () => import('../Walk/Walk.module').then(m => m.WalkModule),
    data: {
        oPermission: {
            permissionId: 'Walk-detail-permissions'
        }
    }
}
];

export const DOG_MODULE_DECLARATIONS = [
    DogHomeComponent,
    DogNewComponent,
    DogDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DogRoutingModule { }