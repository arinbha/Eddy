import type {
  OpenAPIClient,
  Parameters,
  UnknownParamsObject,
  OperationResponse,
  AxiosRequestConfig,
} from "openapi-client-axios";

declare namespace Components {
  namespace Schemas {
    export interface Event {
      name?: string;
      days?: string[];
      location?: /**
       * example:
       * Scaife
       */
      Location;
      /**
       * 24 hour HH:MM time
       * example:
       * 09:30
       */
      start?: string; // \d\d:\d\d
      /**
       * 24 hour HH:MM time
       * example:
       * 16:30
       */
      end?: string; // \d\d:\d\d
    }
    export interface Group {
      /**
       * example:
       * 20
       */
      id?: number; // int64
      users?: User[];
      preferences?: Prefs;
    }
    /**
     * example:
     * Scaife
     */
    export type Location = string;
    export interface Prefs {
      /**
       * The 24-hour number for start time
       * example:
       * 9
       */
      start_time?: number; // int64
      /**
       * The 24-hour number for end time
       * example:
       * 17
       */
      end_time?: number; // int64
    }
    export interface RoomStatus {}
    export type Schedule = Event[];
    export interface User {
      /**
       * example:
       * 10
       */
      id?: number; // int64
      username?: string;
      preferences?: Prefs;
    }
  }
}
declare namespace Paths {
  namespace Book {
    namespace Post {
      export interface RequestBody {
        /**
         * example:
         * GHC 6 Commons
         */
        room?: string;
        /**
         * example:
         * 10
         */
        id?: number; // int64
        /**
         * example:
         * false
         */
        is_group?: boolean;
        /**
         * 24 hour HH:MM time
         * example:
         * 09:30
         */
        start_time?: string; // \d\d:\d\d
        /**
         * 24 hour HH:MM time
         * example:
         * 16:30
         */
        end_time?: string; // \d\d:\d\d
      }
      namespace Responses {
        /**
         * example:
         * Success
         */
        export type $200 = string;
      }
    }
  }
  namespace Login {
    namespace Post {
      export interface RequestBody {
        username?: string;
        password?: string;
      }
      namespace Responses {
        export type $200 = Components.Schemas.User;
        export interface $401 {}
      }
    }
  }
  namespace Newuser {
    namespace Post {
      export interface RequestBody {
        username?: string;
        password?: string;
      }
      namespace Responses {
        export type $200 = Components.Schemas.User;
      }
    }
  }
  namespace Search {
    namespace Get {
      namespace Parameters {
        export interface Prefs {
          prefs?: Components.Schemas.Prefs;
          /**
           * example:
           * 10
           */
          id?: number; // int64
          /**
           * example:
           * false
           */
          is_group?: boolean;
        }
      }
      export interface QueryParameters {
        prefs?: Parameters.Prefs;
      }
      namespace Responses {
        export type $200 = string[];
      }
    }
  }
  namespace UpdateStatus {
    namespace Post {
      export interface RequestBody {
        /**
         * example:
         * GHC 6 Commons
         */
        room?: string;
        status?: Components.Schemas.RoomStatus;
      }
      namespace Responses {
        /**
         * example:
         * Success
         */
        export type $200 = string;
      }
    }
  }
  namespace User$UserIdPrefs {
    namespace Get {
      namespace Responses {
        export type $200 = Components.Schemas.Prefs;
      }
    }
    namespace Post {
      export type RequestBody = Components.Schemas.Prefs;
      namespace Responses {
        export type $200 = Components.Schemas.Prefs;
      }
    }
  }
  namespace Users$UserId {
    namespace Get {
      namespace Responses {
        export type $200 = Components.Schemas.User;
      }
    }
  }
  namespace Users$UserIdGroups {
    namespace Get {
      namespace Responses {
        export type $200 = Components.Schemas.Group[];
      }
    }
  }
  namespace Users$UserIdGroups$GroupId {
    namespace Delete {
      export type RequestBody = Components.Schemas.Group;
      namespace Responses {
        export interface $200 {}
      }
    }
    namespace Post {
      export type RequestBody = Components.Schemas.Prefs;
      namespace Responses {
        export type $200 = Components.Schemas.Group;
      }
    }
  }
  namespace Users$UserIdGroupsJoin {
    namespace Post {
      /**
       * example:
       * 20
       */
      export type RequestBody = number; // int64
      namespace Responses {
        export interface $200 {}
      }
    }
  }
  namespace Users$UserIdGroupsNew {
    namespace Post {
      export type RequestBody = Components.Schemas.Prefs;
      namespace Responses {
        export type $200 = Components.Schemas.Group;
      }
    }
  }
  namespace Users$UserIdNextEvent {
    namespace Get {
      namespace Responses {
        export interface $200 {
          /**
           * 24 hour HH:MM time
           * example:
           * 09:30
           */
          start_time?: string; // \d\d:\d\d
          /**
           * 24 hour HH:MM time
           * example:
           * 16:30
           */
          end_time?: string; // \d\d:\d\d
          /**
           * example:
           * GHC 6 Commons
           */
          location?: string;
        }
      }
    }
  }
  namespace Users$UserIdSchedule {
    namespace Get {
      namespace Responses {
        export type $200 = Components.Schemas.Schedule;
      }
    }
    namespace Post {
      export type RequestBody = Components.Schemas.Schedule;
      namespace Responses {
        export type $200 = Components.Schemas.Schedule;
      }
    }
  }
}

export interface OperationMethods {}

export interface PathsDictionary {
  ["/login"]: {};
  ["/newuser"]: {};
  ["/users/{userId}"]: {};
  ["/users/{userId}/groups"]: {};
  ["/users/{userId}/groups/new"]: {};
  ["/users/{userId}/groups/{groupId}"]: {};
  ["/users/{userId}/groups/join"]: {};
  ["/user/{userId}/prefs"]: {};
  ["/users/{userId}/schedule"]: {};
  ["/users/{userId}/next_event"]: {};
  ["/search"]: {};
  ["/book"]: {};
  ["/update_status"]: {};
}

export type Client = OpenAPIClient<OperationMethods, PathsDictionary>;
