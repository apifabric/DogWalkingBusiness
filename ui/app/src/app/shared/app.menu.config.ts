import { MenuRootItem } from 'ontimize-web-ngx';

import { BookingCardComponent } from './Booking-card/Booking-card.component';

import { ClientPaymentCardComponent } from './ClientPayment-card/ClientPayment-card.component';

import { DogCardComponent } from './Dog-card/Dog-card.component';

import { DogHistoryCardComponent } from './DogHistory-card/DogHistory-card.component';

import { FeedbackCardComponent } from './Feedback-card/Feedback-card.component';

import { MaintenanceLogCardComponent } from './MaintenanceLog-card/MaintenanceLog-card.component';

import { OwnerCardComponent } from './Owner-card/Owner-card.component';

import { ScheduleCardComponent } from './Schedule-card/Schedule-card.component';

import { ServiceCardComponent } from './Service-card/Service-card.component';

import { WalkCardComponent } from './Walk-card/Walk-card.component';

import { WalkerCardComponent } from './Walker-card/Walker-card.component';

import { WalkerPaymentCardComponent } from './WalkerPayment-card/WalkerPayment-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Booking', name: 'BOOKING', icon: 'view_list', route: '/main/Booking' }
    
        ,{ id: 'ClientPayment', name: 'CLIENTPAYMENT', icon: 'view_list', route: '/main/ClientPayment' }
    
        ,{ id: 'Dog', name: 'DOG', icon: 'view_list', route: '/main/Dog' }
    
        ,{ id: 'DogHistory', name: 'DOGHISTORY', icon: 'view_list', route: '/main/DogHistory' }
    
        ,{ id: 'Feedback', name: 'FEEDBACK', icon: 'view_list', route: '/main/Feedback' }
    
        ,{ id: 'MaintenanceLog', name: 'MAINTENANCELOG', icon: 'view_list', route: '/main/MaintenanceLog' }
    
        ,{ id: 'Owner', name: 'OWNER', icon: 'view_list', route: '/main/Owner' }
    
        ,{ id: 'Schedule', name: 'SCHEDULE', icon: 'view_list', route: '/main/Schedule' }
    
        ,{ id: 'Service', name: 'SERVICE', icon: 'view_list', route: '/main/Service' }
    
        ,{ id: 'Walk', name: 'WALK', icon: 'view_list', route: '/main/Walk' }
    
        ,{ id: 'Walker', name: 'WALKER', icon: 'view_list', route: '/main/Walker' }
    
        ,{ id: 'WalkerPayment', name: 'WALKERPAYMENT', icon: 'view_list', route: '/main/WalkerPayment' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    BookingCardComponent

    ,ClientPaymentCardComponent

    ,DogCardComponent

    ,DogHistoryCardComponent

    ,FeedbackCardComponent

    ,MaintenanceLogCardComponent

    ,OwnerCardComponent

    ,ScheduleCardComponent

    ,ServiceCardComponent

    ,WalkCardComponent

    ,WalkerCardComponent

    ,WalkerPaymentCardComponent

];