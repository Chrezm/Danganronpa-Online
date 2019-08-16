180801 (3.0.1)
* Added /time12

180812 (3.1)
*Added /ddroll, /ddrollp for rolls with modifiers
*Added 'rp_getarea(s)' attributes to restrict /getarea(s)
*Added /toggle_rpgetarea(s) to change the above attribute
*Added /st for staff-only chat
*/g now includes OOC usernames as opposed to charname

180910 (3.2)
*Added reachable areas support with
-/unilock
-/bilock
-/delete_areareachlock
-/restore_areareachlock
*Added proper support for spectators (can talk OOC/use commands/change music&areas/use judge buttons now)
*Added support for IC locking with /iclock
*OOC usernames may no longer include the hostname or global message prefixe
*Fixed /kick crash on unrecognized parameters

190126 (3.3)
*Added AFK kicks
*Added user-initiated timers with
-/timer start
-/timer get
-/timer cancel
*Area lists now only list reachable areas

190225 (3.4)
*Added inter-area OOC communication with /scream
*Added debugging tool /exec
*Added inter-area music setting with /rplay
*Renamed /ddroll -> /roll, /ddrollp -> /rollp

190323 (3.5)
*Added sneak support with /sneak and /reveal
*Added inter-area IC announcements with /globalic, /unglobalic
*Added server custom shownames with /shownames
*Added soundproof area attribute
*Expanded inter-area OOC communication with /knock

190519 (3.6)
*Added support for custom music lists with /music_list
*Added area list reloading with /area_list
*Added character restriction on a per-area basis with /char_restrict
*Added scream ranges on a per-area basis (deprecating soundproof attribute)
*Default server configuration now uses DRO standards

190602 (3.7)
*Added automatic passing messages with /autopass
*Added passage lock transientness with /transient
*Added showname moderation tools
-/showname_freeze
-/showname_history
-/showname_list
-/showname_nuke
-/showname_set
*Enforced showname uniqueness per area
*Fixed /area_kick crash on unrecognized parameters
*Fixed /getareas listing an empty area if only people there are sneaking
*Players on server select no longer count in online playercount, nor in /getarea[s] and /area

190609 (3.8)
*Added movement handicaps with /handicap, /unhandicap
*Added area lights with /lights
*Added blood trails with
-/bloodtrail
-/bloodtrail_clean
-/bloodtrail_list
-/bloodtrail_set
*Added /toggle_shownames to disable receiving server shownames
*Allowed for more DRO client effects being used
*Fixed /autopass not sending messages from or for staff

190618 (first with date version system) (3.9)
*Added area descriptions with /look, /look_set
*Console now displays server opening/closing/reconnecting messages.
*Python errors now show additional debugging info on server log+client if error came as a result of command
*Renamed some commands
-allow_iniswap -> /can_iniswap
-delete_areareachlock -> /passage_clear
-restore_areareachlock -> /passage_restore
-toggle_areareachlock -> /can_passagelock
-toggleglobal -> /toggle_global
-toggle_rollp -> /can_rollp
-toggle_rpgetarea -> /can_rpgetarea
-toggle_rpgetareas -> /can_rpgetareas
*Reworked /area_kick so that it now allows area names as parameter
*Reworked /discord so that it now shows the server's Discord server invite link
*Fixed /autopass sending old character name in case of forced char switch on area change
*Fixed /bloodtrail_set not enforcing staff member rank
*Fixed /disemconsonant and /remove_h not working/crashing
*Fixed /follow allowing to follow yourself
*Fixed "Knock" client effect not being sent

190630 (3.10)
*Added support for user initiated day cycles with 
-/clock
-/clock_cancel
-/clock_pause
-/clock_unpause
*Added various moderation tools
-/judgelog
-/shoutlog
-/version
-/whereis
*Added 'has_lights' parameters to areas to allow/disallow using /lights
*Enforced different staff passwords on server configuration
*Shouts now show character used as opposed to OOC name
*Turning lights on reveals who is bleeding and not sneaking
*Fixed area lists allowing for empty parameters
*Fixed blood announcements sent to wrong areas occasionally
*Fixed /kick requiring no arguments
*Fixed music flood guard crash
*Fixed server ghosting on master server list on incorrect server closing
*Fixed pre2.2.5 clients being unable to join

190708 (3.11)
*Added various moderation/debugging tools
-/lasterror
-/multiclients
-/whois
*Added area parameters to allow for non-staff use of custom backgrounds/music
*Added /toggle_allrolls so staff get roll notifications from other areas
*Day cycle notifications now send 'CL' packets to clients
*GMs can no longer /area_kick users from lobby areas
*Renamed timer commands
-/timer start -> /timer
-/timer get -> /timer_get
-/timer cancel -> /timer_cancel
*Fixed a player not unfollowing a player who disconnects and then crashing on area change
*Fixed /roll crashing on too many arguments

190721 (3.12)
*Added global IC prefixes with /globalic_pre
*Added first person mode with /toggle_fp
*Banned players now receive 'You are banned from this server' notifications on attempting to join+Notifies mods of this attempt
*Global IC messages now send notifications on each use
*Made daily gmpasses optional
*Multiple players may now follow the same player
*Renamed some commands from /toggle to /can
*Fixed clients being able to join too quickly on server select and crashing

190801 (4.0)
*Added party support so players move with one another automatically with
-/party
-/party_disband
-/party_id
-/party_invite
-/party_join
-/party_kick
-/party_lead
-/party_list
-/party_members
-/party_uninvite
-/party_unlead
*Added HDID bans with /banhdid, /unbanhdid
*CMs now get IPIDs in /getarea(s), /showname_list and /whois, as well as HDID in /whois
*Iniswapped folders are now shown with /whois
*Fixed security issue with webAO
*TsuserverDR now uses semantic versioning.

190801b (4.0.1)
*Introduced CI testing on Travis

190802 (4.0.3)
*Fixed server player limit not being enforced

190805 (4.0.4)
*Fixed invalid characters crash with /area_list and /music_list

190806 (4.0.5)
*Fixed logging in to a second rank making you keep the first one

1908?? (4.1)
*Added sense block support with
-/blind
-/deaf
-/gag
*Added /bloodtrail_smear to smear blood trails in the area
*Renamed /mutepm -> /toggle_pm
*Fixed /pm not sending complete character names to recipient
*Minor changes to messages sent on area change
-Staff now receive autopass messages if lights are off instead of regular lights off messages
-Reworded messages sent if someone arrives/leaves while bleeding/lights off and sneaking
-Players now receive special notification if there is blood in the area and lights are off
*Fixed blood cleaning sending notification with lights on