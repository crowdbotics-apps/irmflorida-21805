import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import Tutorial154380Navigator from '../features/Tutorial154380/navigator';
import NotificationList154352Navigator from '../features/NotificationList154352/navigator';
import Settings154351Navigator from '../features/Settings154351/navigator';
import Settings154343Navigator from '../features/Settings154343/navigator';
import UserProfile154341Navigator from '../features/UserProfile154341/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
Tutorial154380: { screen: Tutorial154380Navigator },
NotificationList154352: { screen: NotificationList154352Navigator },
Settings154351: { screen: Settings154351Navigator },
Settings154343: { screen: Settings154343Navigator },
UserProfile154341: { screen: UserProfile154341Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
