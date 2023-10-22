//
//  ViewController.m
//  Wifi Beater
//
//  Created by Julio César Rocha on 10/20/23.
//

#import "ViewController.h"

#import <objc/runtime.h>

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}

//https://stackoverflow.com/questions/2053114
- (IBAction)wifiSwitchToggled:(id)sender {
    
    // https://github.com/nanotech/iphoneheaders/blob/master/SpringBoard/SBWiFiManager.h
    //[[objc_getClass("SBWiFiManager") sharedInstance] setWiFiEnabled:NO];
}

@end
