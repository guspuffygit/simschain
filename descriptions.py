import json

interaction_descriptions = {
    "mixer_social_AttemptToScare_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is attempting to scare {target}."
        ]
    },
    "mixer_social_NoxiousCloud_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is rudely farting near {target} as a prank."
        ]
    },
    "mixer_Baby_ShowOff": {
        "pre_actions": [
            "{initiator} is excitingly showing their new baby to {target}."
        ]
    },
    "mixer_ScienceTable_Empty": {
        "pre_actions": [
            "{initiator} is approaching {target} with an empty flask, preparing for a scientific experiment."
        ]
    },
    "mixer_Social_GetToKnow_Friendly_STC": {
        "pre_actions": [
            "{initiator} is initiating a conversation with {target} in an effort to get to know them better."
        ]
    },
    "mixer_social_AskDueDate_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is asking {target} cruelly about their due date, even though they are not pregnant."
        ]
    },
    "mixer_social_GossipAbout_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in friendly gossip with {target}, discussing various topics and sharing information."
        ]
    },
    "mixer_social_AirHorn_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is playfully pranking {target} by continuously blasting an air horn in their face."
        ]
    },
    "mixer_social_SlapEmSilly_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is mischievously slapping {target} silly."
        ]
    },
    "mixer_social_ShareConspiracyTheory_targeted_mischief_alwaysOn": {
        "pre_actions": [
            "{initiator} is sharing a conspiracy theory with {target} in a mischievous manner."
        ]
    },
    "mixer_social_RevealEvilPlans_targeted_mischief_traits": {
        "pre_actions": [
            "{initiator} is mischievously revealing their evil plans to {target}."
        ]
    },
    "mixer_socials_TellJoke_group_Funny_alwaysOn": {
        "pre_actions": [
            "{initiator} is telling a funny joke to {target}."
        ]
    },
    "mixer_social_DoAnImpression_targeted_funny_alwaysOn": {
        "pre_actions": [
            "{initiator} is doing a hilarious impression for {target}, trying to make them laugh."
        ]
    },
    "mixer_social_PlayAPrank_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is playfully pranking {target} with a hand buzzer."
        ]
    },
    "mixer_social_Insult_Mean_STC": {
        "pre_actions": [
            "{initiator} is hurling mean, hurtful insults at {target}."
        ]
    },
    "mixer_social_OfferRose_targeted_romance_emotionSpeficic": {
        "pre_actions": [
            "{initiator} is offering a rose to {target}, expressing their romantic interest."
        ]
    },
    "mixer_social_PassionateKiss_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is leaning in, passionately kissing {target}."
        ]
    },
    "mixer_social_BeEnticing_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is flirting with {target} in an attempt to be sexually enticing."
        ]
    },
    "mixer_social_SexyPose_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is striking a sexy pose, trying to impress and seduce {target}."
        ]
    },
    "mixer_social_SweetTalk_targeted_romance_skills": {
        "pre_actions": [
            "{initiator} is sweet talking {target}, trying to ignite a romantic spark between them."
        ]
    },
    "mixer_social_BoldPickUpLine_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is confidently approaching {target} with a bold pick-up line, hoping to spark some romance."
        ]
    },
    "mixer_social_SuaveKiss_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is confidently leaning in and kissing {target} in a suave and romantic gesture."
        ]
    },
    "mixer_social_FrenziedKiss_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is passionately kissing {target} in a moment of frenzy."
        ]
    },
    "mixer_social_ReciteLovePoetry_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is passionately reciting love poetry to {target}."
        ]
    },
    "mixer_social_Serenade_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is serenading {target} with a romantic song."
        ]
    },
    "mixer_social_MakeAFlirtatiousJoke_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is playfully flirting with {target}, making a joke that is adding a touch of romance to the conversation."
        ]
    },
    "mixer_social_DenounceFriendship_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} is confronting {target} and cruelly denouncing their friendship."
        ]
    },
    "mixer_social_ChewOut_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} is confronting {target} and giving them a harsh scolding."
        ]
    },
    "mixer_social_Provoke_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} is deliberately trying to upset {target} by provoking them."
        ]
    },
    "mixer_social_ThrowDrink_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} is spitefully throwing a drink at {target}."
        ]
    },
    "mixer_social_InsultFace_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} is insulting {target}'s face."
        ]
    },
    "mixer_social_ImpishlyPester_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} is playfully pestering {target} in a mischievous and somewhat mean-spirited manner."
        ]
    },
    "mixer_social_TellDirtyJoke_targeted_funny_emotionSpecific": {
        "pre_actions": [
            "{initiator} is telling a dirty joke to {target}, making them laugh."
        ]
    },
    "mixer_social_FlashCrazyEyes_targeted_funny_emotionSpecific": {
        "pre_actions": [
            "{initiator} is playfully flashing their crazy eyes at {target}, making them burst into laughter."
        ]
    },
    "mixer_social_Vent_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is venting to {target} about their frustrations or concerns."
        ]
    },
    "mixer_social_ComplainAboutProblems_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is expressing their concerns and complaining about their problems to {target}."
        ]
    },
    "mixer_social_AskForAdvice_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is approaching their friend {target} and asking for advice."
        ]
    },
    "mixer_social_ProposeCrazyScheme_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is approaching {target} and proposing a crazy scheme."
        ]
    },
    "mixer_social_PitchStoryIdea_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is pitching a story idea to {target}, hoping to spark their interest."
        ]
    },
    "mixer_social_DescribeNewInvention_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is excitedly describing their new invention to {target}."
        ]
    },
    "mixer_social_SelfDeprecatingJoke_group_funny_emotionSpecific": {
        "pre_actions": [
            "{initiator} is telling a self-deprecating joke about themselves to {target}."
        ]
    },
    "mixer_social_AskAboutCareer_friendly_STC": {
        "pre_actions": [
            "{initiator} is asking {target} about their career."
        ]
    },
    "mixer_social_DiscussInterests_friendly_STC": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly conversation about their interests."
        ]
    },
    "mixer_social_HeartfeltCompliment_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is complimenting {target} in a sincere and friendly manner."
        ]
    },
    "mixer_social_BrightenDay_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is interacting with {target} in a friendly manner, trying to brighten their day."
        ]
    },
    "mixer_social_CheerUp_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is attempting to cheer up {target} in a friendly manner."
        ]
    },
    "mixer_social_GushAboutPartner_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is excitedly talking about their partner with {target}, expressing their love and admiration."
        ]
    },
    "mixer_social_GiveRelationshipAdvice_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is offering relationship advice to {target} in a friendly manner."
        ]
    },
    "mixer_social_AskAboutLoveLife_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is asking {target} about their love life."
        ]
    },
    "mixer_social_EnthuseAboutInterests_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is enthusiastically talking to {target} about their shared interests."
        ]
    },
    "mixer_social_HipBump_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is playfully bumping hips with {target} in a friendly manner."
        ]
    },
    "mixer_social_GivePepTalk_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is boosting {target}'s morale with a friendly pep talk."
        ]
    },
    "mixer_social_ShowOffMuscles_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is flexing their muscles to impress {target}."
        ]
    },
    "mixer_social_RantAndRave_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is expressing their frustrations and opinions to {target}, in a friendly manner."
        ]
    },
    "mixer_social_Seduce_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is attempting to seduce {target} in a romantic way."
        ]
    },
    "mixer_social_Apologize_targeted_friendly_lowScore": {
        "pre_actions": [
            "{initiator} is approaching {target} and apologizing for something, trying to mend their relationship."
        ]
    },
    "mixer_social_AskToBeBoyfriend_targeted_romance_relationship": {
        "pre_actions": [
            "{initiator} is asking {target} to be their boyfriend/girlfriend."
        ]
    },
    "mixer_social_AskToBeGirlfriend_targeted_romance_relationship": {
        "pre_actions": [
            "{initiator} is asking {target} to be their girlfriend, expressing their romantic interest."
        ]
    },
    "mixer_social_FirstKiss_targeted_romance_STC": {
        "pre_actions": [
            "{initiator} is leaning in and sharing their first kiss with {target}."
        ]
    },
    "mixer_social_BreakUp_targeted_mean_relationship": {
        "pre_actions": [
            "{initiator} is breaking up with {target} to end their relationship."
        ]
    },
    "mixer_social_Divorce_targeted_mean_relationship": {
        "pre_actions": [
            "{initiator} and {target} are deciding to end their marriage and get a divorce."
        ]
    },
    "mixer_social_DeclareEnemy_targeted_mean_relationship": {
        "pre_actions": [
            "{initiator} is confronting {target} and declaring them an enemy, negatively affecting their relationship."
        ]
    },
    "mixer_social_Fight_targeted_mean": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument, exchanging insults and trading blows."
        ]
    },
    "mixer_social_Propose_targeted_romance_relationship": {
        "pre_actions": [
            "{initiator} is proposing to {target}, taking their relationship to the next level."
        ]
    },
    "mixer_social_WooHoo_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} is initiating a romantic encounter with {target}."
        ]
    },
    "mixer_social_WooHooInRocketShip_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sharing a romantic moment by having sex in a rocket ship."
        ]
    },
    "mixer_social_WooHooInObservatory_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a romantic encounter in the Observatory."
        ]
    },
    "mixer_social_TryForBaby_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} is initiating a conversation with {target}, trying to establish a friendly connection."
        ]
    },
    "mixer_social_ProfessUndyingLove_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} is expressing their love for {target} in a heartfelt declaration."
        ]
    },
    "mixer_social_TalkAboutDreams_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, discussing their dreams and aspirations."
        ]
    },
    "mixer_social_ShareInsecurities_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is sharing their insecurities with {target}."
        ]
    },
    "mixer_social_BrushOff_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} is rudely brushing off {target}."
        ]
    },
    "mixer_social_YellAT_targeted_mean": {
        "pre_actions": [
            "{initiator} is starting a conversation with {target}."
        ]
    },
    "mixer_social_TryToChat_targeted_friendly_lowScore": {
        "pre_actions": [
            "{initiator} is attempting to chat with {target} in a friendly manner."
        ]
    },
    "mixer_social_FindCommonGround_targeted_friendly_lowScore": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, trying to find common ground."
        ]
    },
    "mixer_social_BegForgiveness_targeted_friendly_lowScore": {
        "pre_actions": [
            "{initiator} is approaching {target} and starting a conversation, hoping to establish a friendly connection."
        ]
    },
    "mixer_social_DescribeRobotInvasion_group_funny_highScore": {
        "pre_actions": [
            "{initiator} is starting a conversation with {target}."
        ]
    },
    "mixer_social_AskForReassurance_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is asking {target} for reassurance, seeking emotional support in their relationship."
        ]
    },
    "mixer_social_RekindleTheRomance_targeted_romance_lowScore": {
        "pre_actions": [
            "{initiator} is trying to rekindle the romance with {target} due to their low relationship score."
        ]
    },
    "mixer_social_WhisperSeductively_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} is whispering seductively to {target}."
        ]
    },
    "mixer_social_AskIfSingle_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} if they're single."
        ]
    },
    "mixer_social_HoldHands_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} is reaching out to {target} and they are holding hands, deepening their romantic bond."
        ]
    },
    "mixer_social_Embrace_targeted_romance_middleScore_STC": {
        "pre_actions": [
            "{initiator} is embracing {target} in a romantic gesture."
        ]
    },
    "mixer_social_Flirt_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is starting to flirt with {target}, hoping to ignite a romantic connection."
        ]
    },
    "mixer_social_ComplimentAppearance_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their appearance."
        ]
    },
    "mixer_social_PickupLine_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is using a pick-up line on {target}."
        ]
    },
    "mixer_social_ConfessAttraction_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} is confessing their attraction to {target}."
        ]
    },
    "mixer_social_CaressCheek_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} is gently caressing {target}'s cheek, expressing a loving gesture."
        ]
    },
    "mixer_social_BlowAKiss_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} is blowing a kiss to {target}, expressing their romantic feelings."
        ]
    },
    "mixer_social_RememberCommonInterests_targeted_romance_lowScore": {
        "pre_actions": [
            "{initiator} is initiating a conversation with {target} to remember their common interests."
        ]
    },
    "mixer_social_FriendlyIntroduction_greetings": {
        "pre_actions": [
            "{initiator} is greeting {target} with a friendly introduction."
        ]
    },
    "mixer_social_FunnyIntroduction_greetings": {
        "pre_actions": [
            "{initiator} is introducing themselves to {target} in a funny and lighthearted way."
        ]
    },
    "mixer_social_RudeIntroduction_greetings": {
        "pre_actions": [
            "{initiator} is rudely introducing themselves to {target} with a cold and unfriendly greeting."
        ]
    },
    "mixer_social_FlirtyIntroduction_greetings_skills": {
        "pre_actions": [
            "{initiator} is greeting {target} in a flirty manner."
        ]
    },
    "mixer_social_CheerfulIntroduction_greetings_skills": {
        "pre_actions": [
            "{initiator} is enthusiastically greeting {target}."
        ]
    },
    "mixer_social_EnchantingIntroduction_greetings_skills": {
        "pre_actions": [
            "{initiator} is introducing themselves to {target} in a friendly and enchanting manner."
        ]
    },
    "mixer_social_DescribeApocalypse_group_mischief_skills": {
        "pre_actions": [
            "{initiator} is describing the apocalypse to {target}."
        ]
    },
    "mixer_social_TellUnbelievableStory_group_friendly_emotionspecific": {
        "pre_actions": [
            "{initiator} is enthusiastically telling {target} an unbelievable story, keeping the conversation light and friendly."
        ]
    },
    "mixer_socials_TellFunnyStory_group_Funny_alwaysOn": {
        "pre_actions": [
            "{initiator} is telling a funny story to {target}, making both of them laugh."
        ]
    },
    "mixer_socials_GoofAround_targeted_Funny_alwaysOn": {
        "pre_actions": [
            "{initiator} is playfully engaging {target} in a silly and lighthearted interaction."
        ]
    },
    "mixer_social_TellOutrageousStory_group_Funny_HighScore": {
        "pre_actions": [
            "{initiator} is telling an outrageous story to {target}, making everyone in the group burst into laughter."
        ]
    },
    "mixer_social_InsideJoke_group_Funny_MediumScore": {
        "pre_actions": [
            "{initiator} is telling {target} an inside joke."
        ]
    },
    "mixer_social_JokeAboutPoliticians_group_Funny_MediumScore": {
        "pre_actions": [
            "{initiator} is telling {target} a joke about politicians."
        ]
    },
    "mixer_social_ImpersonateCelebrity_group_Funny_MediumScore": {
        "pre_actions": [
            "{initiator} is attempting to impersonate a celebrity in a funny way, entertaining the group."
        ]
    },
    "mixer_social_JokeAboutOldTimes_group_Funny_MediumScore": {
        "pre_actions": [
            "{initiator} is reminiscing about old times with {target}, sharing some funny and nostalgic memories."
        ]
    },
    "mixer_social_Intimidate_targeted_mean_middleScore": {
        "pre_actions": [
            "{initiator} is confronting {target} in a mean-spirited attempt to intimidate them."
        ]
    },
    "mixer_social_MockOutfit_targeted_Mean_middleScore": {
        "pre_actions": [
            "{initiator} is mocking {target}'s outfit, being mean-spirited."
        ]
    },
    "mixer_social_ImplyMotherIsLlama_targeted_mean_highScore": {
        "pre_actions": [
            "{initiator} is implying that {target}'s mother is a llama, in a mean-spirited manner."
        ]
    },
    "mixer_social_SitIntimate_MakeAMove_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is sitting with {target} and making a sexual advance on them."
        ]
    },
    "mixer_social_SitIntimate_Kiss_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is leaning in and giving {target} a passionate kiss, expressing their romantic feelings."
        ]
    },
    "mixer_social_SitIntimate_MakeOut_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} is passionately making out with {target}, expressing their romantic feelings."
        ]
    },
    "mixer_social_SitIntimate_GiveMassage_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} is giving {target} a relaxing massage."
        ]
    },
    "mixer_social_SitIntimate_GiveVigorousMassage_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} is giving {target} a vigorous massage, providing a moment of intimate connection."
        ]
    },
    "mixer_social_SitIntimate_AskForMassage_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they could give them a massage."
        ]
    },
    "mixer_social_SitIntimate_WhisperSweetNothings_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} is leaning in close to {target}, whispering sweet nothings in their ear, creating a romantic atmosphere."
        ]
    },
    "mixer_social_SitIntimate_TickleMercilessly_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} is tickling {target} mercilessly, causing them to burst into fits of laughter."
        ]
    },
    "mixer_social_SitIntimate_MakeAMove_targeted_looping": {
        "pre_actions": [
            "{initiator} is initiating a romantic move towards {target} while sitting together."
        ]
    },
    "mixer_social_SitIntimate_Kiss_targeted_looping": {
        "pre_actions": [
            "{initiator} is leaning in and passionately kissing {target}."
        ]
    },
    "mixer_social_SitIntimate_MakeOut_targeted_looping": {
        "pre_actions": [
            "{initiator} is engaging in an intimate make out session with {target} while sitting together."
        ]
    },
    "mixer_social_PretendToBeSlapped_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is pretending to be slapped by {target}."
        ]
    },
    "mixer_social_ClaimCriminalMastermind_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is jokingly claiming to be a criminal mastermind, playfully mischieving with {target}."
        ]
    },
    "mixer_social_StartPreposterousRumor_group_mischief_skills": {
        "pre_actions": [
            "{initiator} is starting a conversation with {target} in order to start a preposterous rumor."
        ]
    },
    "mixer_social_InstillWithFalseConfidence_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is attempting to instill false confidence in {target} with a mischievous motive."
        ]
    },
    "mixer_social_LieAboutCareer_group_mischief_skills": {
        "pre_actions": [
            "{initiator} is telling {target} a false story about their career."
        ]
    },
    "mixer_social_GiveFakeBadNews_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is lying to {target} by telling them fake bad news."
        ]
    },
    "mixer_social_DareToStreak_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is daring {target} to streak naked."
        ]
    },
    "mixer_social_AskAboutDay_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} about their day."
        ]
    },
    "mixer_social_DeepConversation_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} is engaging in a deep conversation with {target}, exchanging their thoughts and opinions."
        ]
    },
    "mixer_social_ExpressAdmiration_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} is expressing their admiration for {target}."
        ]
    },
    "mixer_social_ShareSecret_targeted_Friendly_HighScore": {
        "pre_actions": [
            "{initiator} is sharing a secret with {target}."
        ]
    },
    "mixer_social_Flatter_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is beginning to flatter {target}."
        ]
    },
    "mixer_social_Hug_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} is beginning to hug {target}."
        ]
    },
    "mixer_social_TellEngagingStory_group_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} is captivating {target} with an engaging story now."
        ]
    },
    "mixer_social_TellDramaticStory_group_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} is captivating {target} with a dramatic story, captivating everyone in the group."
        ]
    },
    "mixer_social_RevealDeepSecret_targeted_Friendly_HighScore": {
        "pre_actions": [
            "{initiator} is confiding in {target} and revealing a deep secret."
        ]
    },
    "mixer_social_ExpressFondness_targeted_Romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is expressing their fondness for {target} in a romantic way."
        ]
    },
    "mixer_social_BecomePartnersInCrime_targeted_friendly_highScore": {
        "pre_actions": [
            "{initiator} and {target} are becoming partners in crime."
        ]
    },
    "mixer_social_ComplainAboutBoredom_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is complaining to {target} about feeling bored."
        ]
    },
    "mixer_social_SuggestFunActivities_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is suggesting fun activities to {target}, hoping to have some fun together."
        ]
    },
    "mixer_social_DiscussFavoriteRecipes_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} and {target} are discussing their favorite recipes."
        ]
    },
    "mixer_social_DebateBestCaptains_targeted_Friendly_HighScore": {
        "pre_actions": [
            "{initiator} is engaging in a friendly debate with {target} about who the best captains are."
        ]
    },
    "mixer_social_EnthuseAboutNewShow_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} about a new TV show they just discovered."
        ]
    },
    "mixer_social_DiscussFineCuisine_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a friendly conversation about fine cuisine."
        ]
    },
    "mixer_social_PumpUp_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is enthusiastically motivating {target}, pumping up their self esteem."
        ]
    },
    "mixer_social_RileUp_targeted_mean_alwaysOn": {
        "pre_actions": [
            "{initiator} is agitating {target}, trying to make them upset."
        ]
    },
    "mixer_social_ShareMelancholyThoughts_tag_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is opening up to {target} about their melancholic thoughts, seeking comfort and understanding."
        ]
    },
    "mixer_social_ShareIdeas_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly sharing some brilliant ideas with {target}."
        ]
    },
    "mixer_social_EnthuseAboutSpace_targeted_friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about space, discussing their shared interest and sparking a friendly conversation."
        ]
    },
    "mixer_social_TalkAboutArt_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about art."
        ]
    },
    "mixer_social_DiscussFavoriteBand_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is engaging {target} in a friendly conversation about their favorite band."
        ]
    },
    "mixer_social_EnhuseAboutNewAlbums_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about new albums they've discovered."
        ]
    },
    "mixer_social_DismissGoodness_targeted_mean_alwaysOn": {
        "pre_actions": [
            "{initiator} is dismissing {target} with a mean attitude."
        ]
    },
    "mixer_social_BoastAboutFamily_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is proudly talking about their family to {target}."
        ]
    },
    "mixer_social_BroHug_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is giving {target} a warm and friendly bro hug."
        ]
    },
    "mixer_social_BroBump_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is giving {target} a friendly bro bump."
        ]
    },
    "mixer_social_DiscussFavoriteArtist_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly conversation about their favorite artist."
        ]
    },
    "mixer_social_RevealBrilliantInvention_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly showing {target} their brilliant invention."
        ]
    },
    "mixer_social_DiscussLatestBook_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in a friendly discussion with {target} about the latest book they are reading."
        ]
    },
    "mixer_social_DiscussFavoriteAuthors_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly discussion about their favorite authors."
        ]
    },
    "mixer_social_DiscussWorldPeace_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is initiating a friendly conversation with {target} to discuss world peace."
        ]
    },
    "mixer_social_DismissEvilWays_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is trying to convince {target} to dismiss their evil ways and choose a more friendly path."
        ]
    },
    "mixer_socail_DiscussFearOfCommitment_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is initiating a conversation with {target} to discuss their fear of commitment."
        ]
    },
    "mixer_social_EnthuseAboutOutdoors_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} is sharing their excitement and passion for the great outdoors with {target}."
        ]
    },
    "mixer_social_BragAboutPossesions_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is showing off their impressive possessions to {target}, boasting and bragging about their belongings."
        ]
    },
    "mixer_social_ComplainAboutTvSize_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is expressing their dissatisfaction about the size of the TV to {target}."
        ]
    },
    "mixer_social_DiscussGourmetDishes_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly conversation about gourmet dishes."
        ]
    },
    "mixer_social_ShareCookingSecrets_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is excitedly sharing some cooking secrets with {target}."
        ]
    },
    "mixer_social_TalkAboutCooking_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging {target} in a friendly conversation about cooking."
        ]
    },
    "mixer_social_GiveCookingTips_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is sharing some cooking tips with {target}."
        ]
    },
    "mixer_social_Kiss_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} is leaning in and kissing {target} passionately, expressing their deep romantic feelings."
        ]
    },
    "mixer_social_AskAboutFood_targeted_Friendly_alwaysOn_Event": {
        "pre_actions": [
            "{initiator} is asking {target} about their favorite foods."
        ]
    },
    "mixer_social_InviteToFakeParty_targeted_mischief_alwaysOn": {
        "pre_actions": [
            "{initiator} is inviting {target} to a fake party as a mischievous prank."
        ]
    },
    "mixer_social_ShareBigNews_targeted_Friendly_alwaysOn_pregnancy": {
        "pre_actions": [
            "{initiator} is excitedly sharing some big news with {target}."
        ]
    },
    "mixer_social_DiscussFitnessTechniques_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly conversation about fitness techniques."
        ]
    },
    "mixer_social_PracticeFighting_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a friendly practice fight, honing their combat skills together."
        ]
    },
    "mixer_social_AskForLargeLoan_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} for a large loan."
        ]
    },
    "mixer_social_AskForSmallLoan_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} for a small loan."
        ]
    },
    "mixer_social_RepayLoanSmall_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} to repay a small loan with a friendly attitude."
        ]
    },
    "mixer_social_RepayLoanLargeAndSmall_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is repaying a loan they received from {target} in a friendly interaction."
        ]
    },
    "mixer_social_RepayLoanLarge_targeted_Friendly_alwaysOn_Copy": {
        "pre_actions": [
            "{initiator} is kindly giving {target} money, paying back a large loan."
        ]
    },
    "mixer_social_TalkAboutHandiness_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} discussing the topic of handiness."
        ]
    },
    "mixer_social_BragAboutHandiness_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is proudly bragging to {target} about their impressive handiness skills."
        ]
    },
    "mixer_social_MentorHandiness_targeted_Friendly_HighScore": {
        "pre_actions": [
            "{initiator} is sharing some repair tips with {target} to help them improve their handiness skill."
        ]
    },
    "mixer_social_CalmDown_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is attempting to calm down {target} by engaging in a friendly conversation."
        ]
    },
    "mixer_social_AskRisqueQuestion_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} a risqué question."
        ]
    },
    "mixer_social_AskAboutDrink_targeted_Friendly_alwaysOn_Event": {
        "pre_actions": [
            "{initiator} is asking {target} about their preferred drinks during a friendly conversation."
        ]
    },
    "mixer_social_DiscussColorTheory_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly discussion with {target} about color theory."
        ]
    },
    "mixer_social_ComplimentArt_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their art."
        ]
    },
    "mixer_social_DescribeAesthetics_group_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is complimenting {target}'s sense of aesthetics, discussing their favorite designs and styles."
        ]
    },
    "mixer_social_ProvideLogicalSolution_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is suggesting a logical solution to {target}'s problem."
        ]
    },
    "mixer_social_DiscussLogicalPuzzles_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly discussion with {target} about logic puzzles."
        ]
    },
    "mixer_social_RantLogically_targeted_mean_emotionSpecific": {
        "pre_actions": [
            "{initiator} is passionately declaring their thoughts to {target}, explaining their logical viewpoint."
        ]
    },
    "mixer_social_AskToCleanUpToys_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} to help clean up the toys."
        ]
    },
    "mixer_social_DontTalkAboutCrimeClub_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} is avoiding discussing the Crime Club with {target} in a friendly conversation."
        ]
    },
    "mixer_social_Pickpocket_targeted_mischief_career": {
        "pre_actions": [
            "{initiator} is attempting to pickpocket {target} as a mischievous act, possibly related to their career."
        ]
    },
    "mixer_social_Threaten_targeted_mean_career": {
        "pre_actions": [
            "{initiator} is confronting {target} and threatening them, possibly due to a conflict in their careers."
        ]
    },
    "mixer_social_TalkAboutDrinkMaking_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about making drinks."
        ]
    },
    "mixer_social_ShareBartendingSecrets_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} and {target} are sharing mixology secrets in a friendly conversation."
        ]
    },
    "mixer_social_NPC_AskToHangOut_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is inviting {target} to hang out and spend some time together."
        ]
    },
    "mixer_social_TryOutMaterial_targeted_funny_alwaysOn": {
        "pre_actions": [
            "{initiator} is playfully trying out a new material with {target}, resulting in laughter and amusement."
        ]
    },
    "mixer_social_DiscussTheBestViolinist_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging {target} in a friendly discussion about the best violinist."
        ]
    },
    "mixer_social_PraisePianoSonatas_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is enthusiastically talking to {target} about their love for piano sonatas."
        ]
    },
    "mixer_social_EnthuseAboutGuitarSolos_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about amazing guitar solos."
        ]
    },
    "mixer_social_PromisetoDedicateSong_targeted_romance_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is promising to dedicate a song to {target} as a romantic gesture."
        ]
    },
    "mixer_social_KnockKnockJoke_targeted_funny_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is telling a knock knock joke to {target}, making them laugh."
        ]
    },
    "mixer_social_AskAboutFavoriteAuthor_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} and asking them about their favorite author."
        ]
    },
    "mixer_social_EnthuseAboutLambicPentameter_group_Friendly_MiddleScore_skills": {
        "pre_actions": [
            "{initiator} is excitedly sharing their passion for iambic pentameter with {target}."
        ]
    },
    "mixer_social_TellCrowdPleasingStory_group_funny_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is captivating the group with a funny and crowd-pleasing story."
        ]
    },
    "mixer_social_JokeAboutFashion_targeted_funny_alwaysOn_Skills": {
        "pre_actions": [
            "{initiator} is playfully making a fashion joke, leaving {target} in stitches."
        ]
    },
    "mixer_social_InterviewForStory_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} is conducting an interview with {target} to gather information for a news story."
        ]
    },
    "mixer_social_InterviewAboutLife_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} is interviewing {target} about their life, possibly discussing their career or aspirations."
        ]
    },
    "mixer_social_ThankForComing_targeted_Friendly_alwaysOn_Event": {
        "pre_actions": [
            "{initiator} is thanking {target} for coming to the event."
        ]
    },
    "mixer_social_PointOutConstellations_targeted_Friendly_alwaysOn_careers": {
        "pre_actions": [
            "{initiator} is excitedly pointing out constellations to {target}, sharing their knowledge and sparking a friendly conversation."
        ]
    },
    "mixer_social_AskForTypingTips_targeted_Friendly_alwaysOn_child_skill": {
        "pre_actions": [
            "{initiator} is asking {target} for tips on typing, in a friendly manner."
        ]
    },
    "mixer_social_TalkAboutSchool_targeted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a friendly conversation about school."
        ]
    },
    "mixer_socials_GoofAround_targeted_Funny_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} and {target} are playfully joking around and having a good time together."
        ]
    },
    "mixer_social_PopCultureReference_tareted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} is excitedly sharing a pop culture reference with {target}, sparking a friendly conversation."
        ]
    },
    "mixer_social_TalkAboutFractions_targeted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about fractions."
        ]
    },
    "mixer_social_TellMakeBelieveStory_targeted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} is telling {target} a fun and imaginative story, creating a friendly and playful atmosphere."
        ]
    },
    "mixer_social_DescribeImaginayFriend_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} is explaining to {target} about their imaginary friend, sharing their excitement and childlike imagination with each other."
        ]
    },
    "mixer_social_AskImpossibleRiddle_targeted_mischief_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} is playfully asking {target} an impossible riddle, mischievously teasing them."
        ]
    },
    "mixer_social_DiscussLatestGames_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, discussing the latest games."
        ]
    },
    "mixer_social_MockSimsMood_targeted_mean_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} is mocking {target}'s mood, being mean and insensitive."
        ]
    },
    "mixer_social_DebateGameStrategy_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly debate with {target} about game strategy."
        ]
    },
    "mixer_social_BragAboutSkillz_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} is proudly showing off their impressive skills to {target}, in a friendly manner."
        ]
    },
    "mixer_social_TalkAboutNewApp_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a friendly conversation about a new app."
        ]
    },
    "mixer_social_BragAboutStartup_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} is proudly talking about their successful startup to {target}, sharing their accomplishments and career aspirations."
        ]
    },
    "mixer_social_SecretVillainHandshake_targeted_mean_alwaysOn_career": {
        "pre_actions": [
            "{initiator} is initiating a secret villain handshake with {target}, displaying their mean streak."
        ]
    },
    "mixer_social_TranquilizingHandshake_targeted_mischief_alwaysOn_career": {
        "pre_actions": [
            "{initiator} is playfully tricking {target} with a tranquilizing handshake."
        ]
    },
    "mixer_social_HeckleMicrophonePerformance_alwaysOn": {
        "pre_actions": [
            "{initiator} is playfully heckling {target} during their microphone performance."
        ]
    },
    "mixer_social_GossipAboutVideoGamePros_targeted_friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about video game pros."
        ]
    },
    "mixer_social_ImpressWithVideoGameProwess_targeted_romance_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is impressing {target} with their video game prowess."
        ]
    },
    "mixer_social_MakeFunOfNoobs_targeted_funny_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is teasing {target} in a playful manner, making fun of their lack of experience."
        ]
    },
    "mixer_social_HilariousIcebreaker_greetings": {
        "pre_actions": [
            "{initiator} is breaking the ice with a hilarious greeting, making {target} burst out in laughter."
        ]
    },
    "mixer_social_FunniestJokeInTheWorld_group_Funny_HighScore": {
        "pre_actions": [
            "{initiator} is sharing the funniest joke in the world with {target}, making everyone burst out laughing."
        ]
    },
    "mixer_social_ComplainAboutBills_targeted_Friendly_alwaysOn_bills": {
        "pre_actions": [
            "{initiator} is complaining to {target} about the high cost of bills, hoping for some sympathy or advice."
        ]
    },
    "mixer_social_ComplainAboutLackOfWater_targeted_friendly_alwaysOn_bills": {
        "pre_actions": [
            "{initiator} is expressing frustration to {target} about the lack of water, hoping to find a solution."
        ]
    },
    "mixer_social_ComplainAboutLackOfPower_targeted_friendly_alwaysOn_billsLack": {
        "pre_actions": [
            "{initiator} is voicing their frustration to {target} about the lack of power and the increasing bills."
        ]
    },
    "mixer_social_SitIntimate_Cuddle_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is inviting {target} to sit down and cuddle together in a friendly and intimate manner."
        ]
    },
    "mixer_social_SitIntimate_Cuddle_targeted_looping": {
        "pre_actions": [
            "{initiator} is initiating a cuddle with {target}."
        ]
    },
    "mixer_social_WeaponizedJoke_targeted_funny_alwaysOn": {
        "pre_actions": [
            "{initiator} is telling a weaponized joke to {target}, hoping to make them laugh."
        ]
    },
    "mixer_social_HorrifyingJoke_targeted_funny_alwaysOn": {
        "pre_actions": [
            "{initiator} is telling a horrifying joke to {target}, hoping to get a laugh."
        ]
    },
    "mixer_social_WritingJournalism_ArticleNegative_YellAT_targeted_mean": {
        "pre_actions": [
            "{initiator} is confronting {target} about a negative article, angrily expressing their dissatisfaction."
        ]
    },
    "mixer_social_WritingJournalism_ArticlePositive_Thanks_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their recent article, expressing gratitude and positivity."
        ]
    },
    "mixer_social_AskOnDateEvent_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} on a date, hoping to spend some romantic time together."
        ]
    },
    "mixer_social_CriticizeWooHooTechniques_targeted_mean_middleScore": {
        "pre_actions": [
            "{initiator} is criticizing {target}."
        ]
    },
    "mixer_social_Congratulate_targeted_Friendly_alwaysOn_event": {
        "pre_actions": [
            "{initiator} is congratulating {target} on [keyword that triggered the congratulation]."
        ]
    },
    "mixer_social_ShareBurden_targeted_Friendly_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} is opening up to {target} and sharing their burden, seeking comfort and support."
        ]
    },
    "mixer_social_Beguile_targeted_romance_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} is charming {target} with their flirtatious words and captivating personality."
        ]
    },
    "mixer_social_LendEmotionalSupportNEW_targeted_Friendly_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} is showing kindness and offering emotional support to {target}."
        ]
    },
    "mixer_social_PlantSeedsOfDoubt_targeted_mischief_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} is mischievously trying to plant doubts in {target}'s mind about something."
        ]
    },
    "mixer_social_TellAViciousRumor_targeted_mischief_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} is spreading a malicious rumor about {target}, causing mischief and potentially damaging their reputation."
        ]
    },
    "mixer_social_SubtleyDebase_targeted_mischief_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} is slyly insulting {target} as a mischievous act."
        ]
    },
    "mixer_social_Sabotage_targeted_mischief_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} is trying to sabotage {target}'s plans, using mischief to disrupt their progress."
        ]
    },
    "mixer_social_ComplimentColorChoices_targeted_Friendly_alwaysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their beautiful color choices."
        ]
    },
    "mixer_social_DiscussZebras_targeted_Friendly_alwaysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} discussing zebras."
        ]
    },
    "mixer_social_JokeAboutPenguins_targeted_Friendly_alwaysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} is playfully joking about penguins with {target} in a light-hearted conversation."
        ]
    },
    "mixer_social_DiscussLackOfNewspapers_targeted_Friendly_alwysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} is expressing their concern to {target} about the lack of newspapers in a friendly conversation due to the always-on situation."
        ]
    },
    "mixer_social_ComplimentCostume_targeted_Friendly_alwaysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} is admiring {target}'s costume and complimenting them."
        ]
    },
    "mixer_social_InsultCostume_targeted_mean_alwaysOn_situation_Day1DLC": {
        "pre_actions": [
            "{initiator} is insulting {target}'s costume, causing an unpleasant situation."
        ]
    },
    "mixer_social_WrapBaconAroundEverything_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is excitedly sharing their prank idea with {target}, suggesting they should be wrapping bacon around everything as a friendly joke."
        ]
    },
    "mixer_social_BarricadeClassroomWithWaterCups_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is playfully suggesting to {target} that they should be pranking their classmates by barricading the classroom with water cups."
        ]
    },
    "mixer_social_StartAFoodFight_targeted_Friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is suggesting to {target} that they should start a food fight, in a playful and lighthearted manner."
        ]
    },
    "mixer_social_UnleashTheGerbils_targeted_Friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is enthusiastically suggesting to {target} that they should be planning to unleash the gerbils, in a friendly and mischievous manner."
        ]
    },
    "mixer_social_SellTestAnswers_targeted_Friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is suggesting to {target} that selling test answers could be a lucrative prank."
        ]
    },
    "mixer_social_StuffGeeksInLocker_targeted_Friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is playfully planning to stuff geeks in the locker with {target}."
        ]
    },
    "mixer_social_StuffJocksInLocker_targeted_Friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is playfully suggesting a prank to {target}, involving stuffing jocks in lockers."
        ]
    },
    "mixer_AtWork_FoodFight_Prank": {
        "pre_actions": [
            "{initiator} is playfully throwing food at {target}, starting a fun food fight."
        ]
    },
    "mixer_social_LureLlamaInoTheWorkplace_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is planning to lure a llama into the workplace as a friendly prank on {target}."
        ]
    },
    "mixer_social_FakeAlienContact_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} and {target} are playfully planning to prank others by faking an alien contact."
        ]
    },
    "mixer_social_FillBosssOfficeWithBalloons_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is playfully suggesting to {target} the idea of filling their boss' office with balloons as a prank."
        ]
    },
    "mixer_social_FreeTheFrogs_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is excitedly sharing their plans to free the frogs with {target}, hoping to find an ally in their mission."
        ]
    },
    "mixer_social_SillyPuddyInTheMic_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is planning a silly prank involving sticking clay in the mic to play on {target}."
        ]
    },
    "mixer_social_MustachesForArt_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} and {target} are planning a friendly art prank involving mustaches."
        ]
    },
    "mixer_social_MakeAllInvisibleInkVisible_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is playfully suggesting to {target} that they should be working together to make all invisible ink visible, as a playful prank."
        ]
    },
    "mixer_social_HackIntoCoworkersEmail_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is planning to hack into their co-worker, {target}'s email as a friendly prank."
        ]
    },
    "mixer_social_RearrangeKeysOnTheKeyboard_targeted_friendly_alwaysOn_prank": {
        "pre_actions": [
            "{initiator} is playfully suggesting to {target} that they should prank someone by rearranging the keys on a keyboard."
        ]
    },
    "mixer_AtWork_FakeAlienContact": {
        "pre_actions": [
            "{initiator} is pretending to make contact with aliens, leaving {target} bewildered at work."
        ]
    },
    "mixer_AtWork_FillBosssOfficeWithBalloons": {
        "pre_actions": [
            "{initiator} is deciding to play a prank on {target} by filling their boss' office with balloons."
        ]
    },
    "mixer_AtWork_FreeTheFrogs": {
        "pre_actions": [
            "{initiator} is working diligently to free the frogs from captivity."
        ]
    },
    "mixer_AtWork_HackIntoCoworkersEmail": {
        "pre_actions": [
            "{initiator} is sneakily hacking into {target}'s work email."
        ]
    },
    "mixer_AtWork_LureLlamaIntoOffice": {
        "pre_actions": [
            "{initiator} is convincing {target} to come into the office by luring them with the promise of a llama."
        ]
    },
    "mixer_AtWork_MakeAllInvisibleInkVisible": {
        "pre_actions": [
            "{initiator} is discovering a way to make all invisible ink visible, allowing {target} to see the previously hidden messages."
        ]
    },
    "mixer_AtWork_MustachesForArt": {
        "pre_actions": [
            "{initiator} and {target} are chatting about their artistic skills, particularly focusing on their love for mustaches."
        ]
    },
    "mixer_AtWork_RearrangeKeysOnTheKeyboard": {
        "pre_actions": [
            "{initiator} is mischievously rearranging the keys on {target}'s keyboard while at work."
        ]
    },
    "mixer_AtWork_SillyPuddyInTheMic": {
        "pre_actions": [
            "{initiator} is accidentally putting sticky clay in the mic, causing a silly mess at work with {target}."
        ]
    },
    "mixer_social_SmoothRecovery_targeted_romance_alwaysOn_topic": {
        "pre_actions": [
            "{initiator} is trying to smooth things over with {target} after an awkward moment."
        ]
    },
    "mixer_social_TalkAboutBestsellers_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly conversation about their favorite books and bestsellers."
        ]
    },
    "mixer_social_MockMusicTaste_targeted_mean_trait": {
        "pre_actions": [
            "{initiator} is mocking {target}'s music taste, displaying their mean trait."
        ]
    },
    "mixer_social_AskDueDate_targeted_friendly_alwaysOn_Pregnancy": {
        "pre_actions": [
            "{initiator} is asking {target} about their due date, showing friendliness and interest in their pregnancy."
        ]
    },
    "mixer_social_OfferToFeelBaby_targeted_Friendly_alwaysOn_Pregnancy": {
        "pre_actions": [
            "{initiator} is asking {target} if they can feel their baby bump."
        ]
    },
    "mixer_social_AskToBeBestFriends_targeted_Friendly_HighScore": {
        "pre_actions": [
            "{initiator} is asking {target} to become best friends."
        ]
    },
    "mixer_social_DiscussConquests_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, discussing their conquests."
        ]
    },
    "mixer_social_ComplimentOutfit_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is complimenting {target}'s outfit, showing appreciation for their sense of style."
        ]
    },
    "mixer_social_ApologizeInBed_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} is apologizing to {target} in bed."
        ]
    },
    "mixer_social_SitIntimate_WooHoo_targeted_romance_HighScore": {
        "pre_actions": [
            "{initiator} is initiating a romantic encounter with {target}, seeking an intimate and passionate connection."
        ]
    },
    "mixer_social_SitIntimate_TryForBaby_targeted_romance_HighScore": {
        "pre_actions": [
            "{initiator} is initiating a romantic interaction with {target}, hoping to start a family together."
        ]
    },
    "mixer_social_OfferFriendlyMassage_targeted_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} is offering a friendly massage to {target}."
        ]
    },
    "mixer_social_ExposeSupervillain_targeted_mean_career": {
        "pre_actions": [
            "{initiator} is confronting {target} about their secret identity as a Supreme Villain!"
        ]
    },
    "mixer_social_FightSupervillain_targeted_mean_career": {
        "pre_actions": [
            "{initiator} is confronting {target}, who is a supreme villain, in an intense battle due to their mean career."
        ]
    },
    "mixer_social_BegForNewToys_targeted_friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, a child Sim, is approaching {target} in a friendly manner and is politely asking them to buy new toys for them."
        ]
    },
    "mixer_social_ExpressLove_targeted_friendly_AlwaysOn_child": {
        "pre_actions": [
            "{initiator} is affectionately telling {target} that they love them, showing their friendly bond."
        ]
    },
    "mixer_social_TellJoke_group_Funny_alwaysOn_child": {
        "pre_actions": [
            "{initiator} is telling a funny joke to {target} and the rest of the group, making everyone laugh, especially the children."
        ]
    },
    "mixer_social_MakeFunOfAdults_targeted_funny_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, a funny child, is making fun of adults, including {target}."
        ]
    },
    "mixer_social_MakeSillyFace_targeted_funny_alwaysOn_child": {
        "pre_actions": [
            "{initiator} is making a silly face at {target}, trying to be funny and entertain them."
        ]
    },
    "mixer_social_TellGrossJoke_group_funny_MediumScore_child": {
        "pre_actions": [
            "{initiator} is telling a gross joke to {target} and the group is erupting in laughter, although it may not be appropriate for children."
        ]
    },
    "mixer_social_CallNames_targeted_mean_child": {
        "pre_actions": [
            "{initiator} is insulting {target} by calling them mean names."
        ]
    },
    "mixer_social_MonkeyAround_targeted_mischief_alwaysOn_child": {
        "pre_actions": [
            "{initiator} is playfully starting to monkey around with {target}, indulging in mischief like a child."
        ]
    },
    "mixer_social_Annoy_targeted_mean_alwaysOn_childANDteen": {
        "pre_actions": [
            "{initiator} is purposefully annoying {target}, acting mean and childish, possibly as a teenager."
        ]
    },
    "mixer_social_LectureAboutMisbehavior_mean_targeted_alwaysOn_child": {
        "pre_actions": [
            "{initiator} is lecturing {target} about their misbehavior, being mean to them for being a child."
        ]
    },
    "mixer_social_MakeBelieve_targeted_friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a friendly game of make believe, pretending to be characters from their favorite stories."
        ]
    },
    "mixer_social_AskToStayTheNight_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} is asking {target} if they would like to stay the night, hinting at a romantic interest."
        ]
    },
    "mixer_social_AskAboutSchool_targeted_friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking them about school in a friendly manner, showing interest in their education as a child."
        ]
    },
    "mixer_social_InviteTo_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is inviting {target} to join them in a friendly activity."
        ]
    },
    "mixer_social_TeachValuableLesson_targeted_Friendly_HighScore_child": {
        "pre_actions": [
            "{initiator} is patiently teaching {target}, a child Sim, a valuable lesson in a friendly manner."
        ]
    },
    "mixer_Fireplace_WarmSelf": {
        "pre_actions": [
            "{initiator} is sitting in front of the fireplace, enjoying the warmth."
        ]
    },
    "mixer_social_AttemptToSeduce_targeted_romance_middleScore_teenMale": {
        "pre_actions": [
            "{initiator} is trying to seduce {target}, hoping to ignite a romantic connection."
        ]
    },
    "mixer_social_AttemptToSeduce_targeted_romance_MiddleScore_teenFemale": {
        "pre_actions": [
            "{initiator} is trying to seduce {target}, hoping to ignite a romantic connection."
        ]
    },
    "mixer_social_KissNeck_targeted_romance_relationship_teen": {
        "pre_actions": [
            "{initiator} is leaning in and kissing {target}'s neck, expressing their romantic feelings towards them."
        ]
    },
    "mixer_social_Flirt_targeted_romance_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} is playfully flirting with {target}, hoping to ignite a spark of romance between them."
        ]
    },
    "mixer_social_OfferToFeelBaby_Invite_targeted_Friendly_alwaysOn_Pregnancy": {
        "pre_actions": [
            "{initiator} is offering to let {target} feel their baby, inviting them to share in the joy of the pregnancy."
        ]
    },
    "mixer_social_SitIntimate_Snuggle_targeted_looping": {
        "pre_actions": [
            "{initiator} is sitting down next to {target} and is pulling them into a warm and intimate snuggle."
        ]
    },
    "mixer_social_SitIntimate_Snuggle_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is sitting close to {target} and affectionately snuggling up to them, deepening the romantic connection between them."
        ]
    },
    "mixer_social_DemandIndependence_targeted_mean_teen": {
        "pre_actions": [
            "{initiator} is confronting {target}, demanding their independence as a mean teen."
        ]
    },
    "mixer_social_TeaseMercilessly_targeted_mean_teen": {
        "pre_actions": [
            "{initiator} is mercilessly teasing {target}, being particularly mean about it."
        ]
    },
    "mixer_social_ComplainAboutParents_targeted_Friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} is expressing their frustration about their parents to {target}, hoping for some understanding and support."
        ]
    },
    "mixer_social_AskAboutWooHoo_targeted_Friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking them about WooHoo, in a friendly and curious manner."
        ]
    },
    "mixer_social_HighFive_targeted_friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} is giving props to {target}, offering a high five as a friendly gesture."
        ]
    },
    "mixer_social_ShowOffOutfit_targeted_friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} is enthusiastically showing off their new outfit to {target}, hoping to impress them with their style."
        ]
    },
    "mixer_social_GiveTheWooHooTalk_targeted_friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} is sitting down with {target} for a friendly conversation about the birds and the bees."
        ]
    },
    "mixer_social_Gossip_targeted_friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} is excitedly sharing some juicy gossip with {target}, hoping to strengthen their friendship."
        ]
    },
    "mixer_social_TalkAboutBestBait_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, discussing the best bait to use."
        ]
    },
    "mixer_social_BoastAboutBiggestCatch_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} about their biggest catch, bragging about their fishing skills."
        ]
    },
    "mixer_social_ShareFishingTips_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly conversation, sharing fishing tips."
        ]
    },
    "mixer_social_AskOnDateEvent_targeted_romance_alwaysOn_Teen": {
        "pre_actions": [
            "{initiator} is nervously asking {target} on a date, hoping to spend more time together and explore their romantic feelings."
        ]
    },
    "mixer_social_GiveColdShoulder_targeted_mean_Female": {
        "pre_actions": [
            "{initiator}, a mean Sim, is purposefully ignoring {target} and giving them the cold shoulder."
        ]
    },
    "mixer_social_GiveColdShoulder_targeted_mean_Male": {
        "pre_actions": [
            "{initiator} is purposefully ignoring {target}, acting in a mean and unfriendly manner."
        ]
    },
    "mixer_social_KissCheek_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is leaning in and gently kissing {target} on the cheek, expressing a romantic gesture."
        ]
    },
    "mixer_social_TakePictureTogether_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is inviting {target} to take a picture together, creating a friendly and fun moment."
        ]
    },
    "mixer_social_EnthuseAboutCelebrations_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly conversation about various celebrations, enthusiastically discussing their favorite aspects."
        ]
    },
    "mixer_social_EnthuseAboutCakes_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their love for cakes."
        ]
    },
    "mixer_social_AskAboutBeingOld_targeted_Friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking about what it's like to be old, in a friendly manner."
        ]
    },
    "mixer_social_Jeer_targeted_mean_middleScore": {
        "pre_actions": [
            "{initiator} is mocking {target} in a mean-spirited manner."
        ]
    },
    "mixer_social_ComplainAboutEverything_targeted_Friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} is expressing their discontent about everything to {target} in a friendly manner. They are venting their frustrations and sharing their grievances."
        ]
    },
    "mixer_social_KissHands_targeted_romance_emotionSpecific": {
        "pre_actions": [
            "{initiator} is taking {target}'s hand and gently kissing it, a romantic gesture to show affection."
        ]
    },
    "mixer_social_AskMoveIn_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} if they would like to join their household."
        ]
    },
    "mixer_social_GossipAboutNeighbors_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about the neighbors, sharing juicy gossip."
        ]
    },
    "mixer_social_ComplainAboutLocalYouths_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} is politely approaching {target}, their neighbor, to complain about the behavior of some local youths."
        ]
    },
    "mixer_social_DiscussNeighborhoodChanges_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} is approaching {target} in a friendly manner to discuss recent changes in the neighborhood."
        ]
    },
    "mixer_social_ChatAboutPropertyVaules_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} is initiating a friendly conversation with {target} about property values, as they are neighbors."
        ]
    },
    "mixer_social_DiscussLocalFishingSpots_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} is initiating a friendly conversation with {target}, to discuss local fishing spots."
        ]
    },
    "mixer_social_ComplimentHouse_targeted_friendly_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} is complimenting {target}'s house, showing their friendly and neighborly nature."
        ]
    },
    "mixer_social_InsultHouse_targeted_mean_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} is making a mean comment about {target}'s house, angering their neighbor."
        ]
    },
    "mixer_social_InsultYard_targeted_mean_alwaysOn_neighbor": {
        "pre_actions": [
            "{initiator} is angrily insulting {target}'s yard, causing tension between the two neighbors."
        ]
    },
    "mixer_social_TryToPickFight_targeted_mean_middleScore_child": {
        "pre_actions": [
            "{initiator} is attempting to start an argument with {target}, displaying mean and aggressive behavior."
        ]
    },
    "mixer_social_BragAboutGrades_targeted_Friendly_alwaysOn_child_teen": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} about their impressive grades, hoping to impress them."
        ]
    },
    "mixer_social_ComplainAboutClasses_targeted_Friendly_alwaysOn_child_teen": {
        "pre_actions": [
            "{initiator} is approaching {target} and starting to complain about their classes. They seem to be in a friendly conversation, possibly because they are both children or teens."
        ]
    },
    "mixer_social_LectureAboutGrades_targeted_Friendly_alwaysOn_child_teen": {
        "pre_actions": [
            "{initiator} is giving a friendly lecture to {target} about the importance of grades."
        ]
    },
    "mixer_social_PraiseForGoodGrades_targeted_Friendly_alwaysOn_child_teen": {
        "pre_actions": [
            "{initiator} is praising {target} for their good grades, showing their friendly and supportive nature."
        ]
    },
    "mixer_social_KissCheek_targeted_Friendly_MiddleScore_child": {
        "pre_actions": [
            "{initiator} is leaning in and giving {target} a friendly kiss on the cheek."
        ]
    },
    "mixer_social_EnthuseAboutCandy_targeted_Friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their love for candy."
        ]
    },
    "mixer_social_QuoteCartoonCharacter_targeted_Funny_alwaysOn_child": {
        "pre_actions": [
            "{initiator} is impersonating a funny cartoon character, making {target} laugh like a child."
        ]
    },
    "mixer_social_TalkAboutToys_targeted_Friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their favorite toys, sharing playful stories and bonding over shared interests."
        ]
    },
    "mixer_social_TalkAboutFavoriteAnimal_targeted_Friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, discussing their favorite animals."
        ]
    },
    "mixer_social_LectureAboutResponsibilities_targeted_Friendly_alwaysOn_teen": {
        "pre_actions": [
            "{initiator} is giving a friendly lecture to {target} about responsibilities, hoping to guide them in the right direction as a teen."
        ]
    },
    "mixer_social_ExchangePromiseRings_targeted_romance_relationship_teen": {
        "pre_actions": [
            "{initiator} and {target} are exchanging promise rings, symbolizing their commitment to each other in their teenage relationship."
        ]
    },
    "mixer_social_ConvinceToLeaveSpouse_targeted_romance_relationship": {
        "pre_actions": [
            "{initiator} is trying to convince {target} to leave their spouse and pursue a romantic relationship."
        ]
    },
    "mixer_social_SayGoodbye_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is giving a friendly goodbye to {target} as they are parting ways."
        ]
    },
    "mixer_social_BanterWithOldFriend_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in lighthearted banter with {target}, reminiscing about old times and catching up on each other's lives."
        ]
    },
    "mixer_social_SitIntimate_LookDeeplyIntoEyes_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} and {target} are sitting closely together, locking eyes with a deep intensity, and fostering a moment of intimate connection."
        ]
    },
    "mixer_social_SitIntimate_TeaseFlirtatiously_targeted_romance_middleScore": {
        "pre_actions": [
            "{initiator} is sitting next to {target} and playfully teasing them in a flirtatious manner, creating an intimate atmosphere."
        ]
    },
    "mixer_social_AskWhatHappened_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking them what happened, showing concern and being friendly."
        ]
    },
    "mixer_socials_GoofAround_teen_targeted_Funny_alwaysOn": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a lighthearted and funny interaction, goofing around and having a good time."
        ]
    },
    "mixer_social_SitIntimate_LookDeeplyIntoEyes_targeted_looping": {
        "pre_actions": [
            "{initiator} and {target} are sitting together, sharing an intimate moment as they are gazing deeply into each other's eyes."
        ]
    },
    "mixer_Baby_ShowOff_Wait": {
        "pre_actions": [
            "{initiator} is proudly showing off their cute baby to {target} while waiting for something."
        ]
    },
    "mixer_Social_Sim_Ghost_Ask_About_Being_Dead": {
        "pre_actions": [
            "{initiator} is curiously asking {target}, a ghost Sim, about what it's like to be dead."
        ]
    },
    "mixer_social_Ghost_ConsoleAboutDeath_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is consoling {target} about the topic of death, offering a friendly understanding and support."
        ]
    },
    "mixer_social_Ghost_Invite_to_Household_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is warmly inviting {target} to join their household, despite {target} being a ghost."
        ]
    },
    "mixer_Campfire_WarmSelf": {
        "pre_actions": [
            "{initiator} is sitting close to the campfire, basking in the warmth and enjoying their own company."
        ]
    },
    "mixer_social_WooHoo_targeted_romance_transition_Tent": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a romantic encounter inside a tent."
        ]
    },
    "mixer_social_TryForBaby_targeted_romance_transition_Tent": {
        "pre_actions": [
            "{initiator} and {target} are sharing an intimate moment in the tent, hoping to conceive a baby together."
        ]
    },
    "mixer_Campfire_StareIntoFlames": {
        "pre_actions": [
            "{initiator} is sitting beside {target} at the campfire and both of them are gazing into the flames, enjoying the warmth and peaceful atmosphere."
        ]
    },
    "mixer_Campfire_RoastMarshmallows": {
        "pre_actions": [
            "{initiator} is sitting by the campfire and enjoying roasting marshmallows."
        ]
    },
    "mixer_social_GoAway_targeted_mean_alwaysOn": {
        "pre_actions": [
            "{initiator} is rudely telling {target} to go away."
        ]
    },
    "mixer_social_DiscussHydration_targeted_Friendly_Athlete_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about the importance of hydration, especially for athletes."
        ]
    },
    "mixer_social_DiscusssSportsStatistics_targeted_Friendly_Athlete_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about sports statistics, possibly bonding over their shared interest in athletic endeavors."
        ]
    },
    "mixer_social_OffertoPumpup_targeted_Friendly_Athlete_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is approaching {target} and offering to pump them up before their athletic event."
        ]
    },
    "mixer_social_SuggestWorkingOut_targeted_Friendly_Athlete_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is suggesting to {target} that they should be working out together, considering their shared interest in fitness."
        ]
    },
    "mixer_social_MakeFunOfCorporateGoons_Targeted_Funny_AlwaysOn_Career": {
        "pre_actions": [
            "{initiator} is humorously mocking {target}, who is a corporate goon, playing off their career."
        ]
    },
    "mixer_social_ImitateBoss_Targeted_Funny_AlwaysOn_Career": {
        "pre_actions": [
            "{initiator} is playfully imitating their boss to {target} in a funny way, in order to bring some humor to the workplace."
        ]
    },
    "mixer_social_GossipAboutOfficeRomance_Targeted_Friendly_AlwaysOn_Career": {
        "pre_actions": [
            "{initiator} is casually bringing up the topic of office romances while chatting with {target} in a friendly and non-judgmental way, they are genuinely showing interest in this juicy gossip."
        ]
    },
    "mixer_social_Pool_Splash_targeted_alwaysOn": {
        "pre_actions": [
            "{initiator} is jumping into the pool and splashing {target} playfully."
        ]
    },
    "mixer_social_GiveFakeInvestmentTips_Targeted_Mischief_AlwaysOn_career": {
        "pre_actions": [
            "{initiator} is mischievously giving {target} fake investment tips, likely causing chaos and mischief."
        ]
    },
    "mixer_social_OfferCareerAdvice_Targeted_Friendly_AlwaysOn_career": {
        "pre_actions": [
            "{initiator} is offering some career advice to {target} in a friendly and targeted manner."
        ]
    },
    "mixer_social_BragAboutJobTitle_Targeted_Friendly_AlwaysOn_career": {
        "pre_actions": [
            "{initiator} is excitedly bragging about their impressive job title to {target}, hoping to impress them with their career success."
        ]
    },
    "mixer_social_Pickpocket_targeted_mischief_career_household": {
        "pre_actions": [
            "{initiator} is attempting to pickpocket {target} as part of their mischief career or for personal gain."
        ]
    },
    "mixer_social_WooHooInHottub_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking away to the hot tub for some intimate time together, engaging in a romantic WooHoo."
        ]
    },
    "mixer_social_HotTub_Splash_targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is playfully splashing {target} in the hot tub, creating a friendly and fun atmosphere."
        ]
    },
    "mixer_social_EnthuseAboutFruitcake_trageted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their love for fruitcake."
        ]
    },
    "mixer_social_ComplainAbout_Fruitcake_targeted_alwayson": {
        "pre_actions": [
            "{initiator} is expressing their discontent about fruitcake to {target}."
        ]
    },
    "mixer_social_TryForBabyInHottub_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sharing a romantic moment in the hot tub as they are trying for a baby."
        ]
    },
    "mixer_social_TryForBabyInObservatory_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are heading to the observatory for some romantic time together, as they are transitioning into trying for a baby."
        ]
    },
    "mixer_social_TryForBabyInRocketShip_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are passionately entering their rocket ship, ready to try for a baby as their relationship is taking a romantic turn."
        ]
    },
    "mixer_social_TryForBabyinHotTub_targeted_stand_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a romantic encounter in the hot tub, attempting to try for a baby together."
        ]
    },
    "mixer_social_WooHooinHotTub_targeted_Stand_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a passionate WooHoo session in the hot tub, their romantic feelings are transitioning to a new level."
        ]
    },
    "mixer_social_WooHooInBush_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a romantic encounter in the bushes."
        ]
    },
    "mixer_social_GoingOutSocials_Matchmake": {
        "pre_actions": [
            "{initiator} is making a move on {target} while going out, hoping to ignite a romantic connection."
        ]
    },
    "mixer_social_TryForBabyInBush_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into a bush, hoping to start a family together."
        ]
    },
    "mixer_social_GoingOutSocials_TalkUpSim": {
        "pre_actions": [
            "{initiator} is enthusiastically talking up {target} to others, highlighting their positive attributes and achievements."
        ]
    },
    "mixer_social_GoingOutSocials_BreakUpSims": {
        "pre_actions": [
            "{initiator} is confronting {target} in an attempt to break up their relationship."
        ]
    },
    "mixer_social_GoingOutSocials_TrashAnotherSim": {
        "pre_actions": [
            "{initiator} is engaging in trash talk with {target} while socializing at a gathering."
        ]
    },
    "mixer_social_ComplainAboutLackofLoveLife_Targeted_Friendly_AlwaysOn_Jealous_Trait": {
        "pre_actions": [
            "{initiator} is approaching {target} and beginning to vent about their lack of love life. Despite feeling jealous, {target} is listening attentively and offering friendly advice."
        ]
    },
    "mixer_social_Trick_Targeted_Mischief_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is playing a mischievous trick on {target}."
        ]
    },
    "mixer_social_Treat_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is giving {target} a treat, being friendly and showing kindness."
        ]
    },
    "mixer_social_ConsoleAboutDeath_Targeted_Friendly_EmotionSpecific": {
        "pre_actions": [
            "{initiator} is consoling {target} about the topic of death, showing empathy and offering comfort."
        ]
    },
    "mixer_social_EnthuseAbout_ThrillOfTheSteal_friendly_Klepto": {
        "pre_actions": [
            "{initiator} is excitedly sharing their love for the thrill of stealing with {target}, in a friendly conversation."
        ]
    },
    "mixer_social_TalkAboutGrilledCheese_targeted_Friendly_alwaysOn_aspiration": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about Grilled Cheese, as part of their aspiration."
        ]
    },
    "mixer_social_EvangelizeGrilledCheese_Friendly_alwaysOn_Trait": {
        "pre_actions": [
            "{initiator} is enthusiastically sharing their love for grilled cheese with {target}, trying to convince them to also become a grilled cheese enthusiast."
        ]
    },
    "mixer_social_AskAbout_PrizedPossessions_mischief_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} is mischievously asking {target} about their prized possessions."
        ]
    },
    "mixer_VegetarianTrait_EvangelizeVegetarianBenefits": {
        "pre_actions": [
            "{initiator} is trying to convince {target}, who also has the Vegetarian trait, of the various benefits of following a vegetarian lifestyle."
        ]
    },
    "mixer_VegetarianTrait_EnthuseAboutVegetarianism": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their shared vegetarianism and the benefits of a plant-based diet."
        ]
    },
    "mixer_VegetarianTrait_ComplainAboutFlavorlessMeatSubstitutes": {
        "pre_actions": [
            "{initiator} is expressing their dissatisfaction about flavorless meat substitutes to {target}, sharing their frustration as a vegetarian."
        ]
    },
    "mixer_social_AskToSprayForMonsterUnderBed_Friendly_AlwaysOn_Child": {
        "pre_actions": [
            "{initiator} is asking {target} in a friendly manner if they can help spray the monster under the bed."
        ]
    },
    "mixer_social_AskToJustBeFriends_Targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} if they can just be friends, wanting to maintain a friendly relationship."
        ]
    },
    "mixer_AskToSpray_MonsterUnder_Bed": {
        "pre_actions": [
            "{initiator} is bravely approaching {target} and asking if they can help spray the monster lurking under the bed."
        ]
    },
    "mixer_social_CheerUp_targeted_Friendly_alwaysOn_TragicClown": {
        "pre_actions": [
            "Tragically, {initiator} is trying to cheer up {target} by being friendly and engaging in conversation."
        ]
    },
    "mixer_social_Toddler_Mean_Yell_At": {
        "pre_actions": [
            "{initiator} is angrily yelling at the {target} toddler in a mean manner."
        ]
    },
    "mixer_social_Toddler_Funny_Say_NonSense": {
        "pre_actions": [
            "{initiator} is starting to babble nonsense to {target}, trying to be funny and entertain them."
        ]
    },
    "mixer_social_Toddler_Funny_Tell_Knock_Knock_Joke": {
        "pre_actions": [
            "{initiator} is excitedly approaching {target} and telling a hilarious knock knock joke, hoping to make them laugh."
        ]
    },
    "mixer_socials_Toddler_Ask_Why_Friendly": {
        "pre_actions": [
            "{initiator} is asking {target} why, in a friendly manner, as part of their social interaction with a toddler Sim."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Favorite_Color": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} about their favorite color."
        ]
    },
    "mixer_socials_Toddler_TalkAbout_Favorite_Animal": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} about their favorite animal."
        ]
    },
    "mixer_socials_Toddler_TalkAbouts_Party": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} about parties."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Art": {
        "pre_actions": [
            "{initiator} is attempting to talk to {target} about art, but it may be proving difficult for a toddler to engage in such a conversation."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Day": {
        "pre_actions": [
            "{initiator} is trying to engage {target} in a conversation about their day."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Dinosaurs": {
        "pre_actions": [
            "{initiator}, a toddler, is excitedly talking to {target} about dinosaurs."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Superheroes": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their favorite superheroes."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Princesses": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about princesses, sharing their favorite stories and Disney movies."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Tell_Story": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} and is beginning to tell a story."
        ]
    },
    "mixer_social_Toddler_Friendly_TalkTo_Stranger": {
        "pre_actions": [
            "{initiator} is approaching a stranger, {target}, and engaging in a friendly conversation."
        ]
    },
    "mixer_social_Toddler_TalkAbout_Tell_Goofy_Story": {
        "pre_actions": [
            "{initiator} is excitedly telling a goofy story to {target} during their conversation."
        ]
    },
    "mixer_social_toddler_Funny_JokeAboutChickenButt": {
        "pre_actions": [
            "{initiator}, a toddler, is telling a funny joke to {target} about chicken butts."
        ]
    },
    "mixer_socials_Toddler_Ask_AboutWorld_Friendly_Inquisitive": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, asking about the world and showing genuine curiosity."
        ]
    },
    "mixer_social_Targeted_Mean_AlwaysOn_STC_Toddler_Scold": {
        "pre_actions": [
            "{initiator} is scolding {target} for misbehaving, using a harsh tone."
        ]
    },
    "mixer_social_Targeted_Mean_AlwaysOn_STC_Toddler_YellAt": {
        "pre_actions": [
            "{initiator} is directing their anger towards {target}, yelling at them in a mean-spirited manner, even though {target} is just a toddler."
        ]
    },
    "mixer_social_Targeted_Mean_AlwaysOn_STC_Toddler_CrushDreams": {
        "pre_actions": [
            "{initiator} is cruelly targeting {target} by crushing their dreams, displaying mean behavior towards them, despite {target} being just a toddler."
        ]
    },
    "mixer_socials_Toddler_TalkAbouts_Trucks": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} about trucks."
        ]
    },
    "mixer_social_AskAboutDay_targeted_Friendly_alwaysOn_Toddler": {
        "pre_actions": [
            "{initiator}, a friendly toddler, is asking {target} about their day."
        ]
    },
    "mixer_Social_GetToKnow_Friendly_STC_TargetToddler": {
        "pre_actions": [
            "{initiator} is approaching {target} with a friendly smile, eager to get to know them better."
        ]
    },
    "mixer_socials_TellFunnyStory_group_Funny_alwaysOn_toddler": {
        "pre_actions": [
            "{initiator} is joining a group and is telling a funny story to entertain everyone, including the toddler."
        ]
    },
    "mixer_social_BrightenDay_targeted_friendly_emotionSpecific_toddlerOnly": {
        "pre_actions": [
            "{initiator} is approaching {target} with a smile and playfully trying to brighten their day. This interaction is only being available when {target} is a toddler."
        ]
    },
    "mixer_social_MakePeaceAfterFight": {
        "pre_actions": [
            "{initiator} is apologizing and trying to make peace with {target} after their fight."
        ]
    },
    "mixer_social_CheerUp_targeted_friendly_emotionSpecific_c2a": {
        "pre_actions": [
            "{initiator} is attempting to cheer up {target} by engaging in a friendly conversation and offering support."
        ]
    },
    "mixer_social_ConsoleAboutDeath_Targeted_Friendly_EmotionSpecific_c2a": {
        "pre_actions": [
            "{initiator} is consoling {target} about death, offering their support and comforting words."
        ]
    },
    "mixer_social_DiscussCostume_targeted_Friendly": {
        "pre_actions": [
            "{initiator} is beginning a friendly conversation with {target} to discuss their costume."
        ]
    },
    "mixer_social_ComplimentCostume_Targeted_Friendly": {
        "pre_actions": [
            "{initiator} is complimenting {target}'s costume, giving them a friendly and targeted compliment."
        ]
    },
    "mixer_social_QuestionCostume_Targeted_Mean": {
        "pre_actions": [
            "{initiator} is confronting {target} about their costume, in a mean-spirited way."
        ]
    },
    "mixer_social_SayGoodbye_targeted_Friendly_alwaysOn_Toddler": {
        "pre_actions": [
            "{initiator} is waving and saying goodbye to {target} in a friendly manner."
        ]
    },
    "mixer_social_WhatsYourProblem_Targeted_Mean_Sentiments": {
        "pre_actions": [
            "{initiator} is confronting {target} and asking what their problem is, expressing mean sentiments towards them."
        ]
    },
    "mixer_social_AskForAdvice_targeted_friendly_emotionSpecific_Scared": {
        "pre_actions": [
            "{initiator} is approaching {target} and nervously asking for encouragement, seeking some friendly advice."
        ]
    },
    "mixer_social_GoodTrait_HelpOut": {
        "pre_actions": [
            "{initiator} is using their good trait to offer help to {target}."
        ]
    },
    "mixer_social_TalkItOut_targeted_romance_alwaysOn_JealousTrait": {
        "pre_actions": [
            "{initiator} and {target} are having a sit-down conversation to talk through their issues, possibly addressing any romantic tensions or jealousy that may arise due to certain traits."
        ]
    },
    "mixer_socials_BragAboutBaby_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their adorable baby, wanting to share their joy and pride."
        ]
    },
    "mixer_socials_GossipAboutOtherParents_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about other parents, sharing some gossip and juicy stories."
        ]
    },
    "mixer_social_ShareBabyPictures_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is excitedly showing {target} adorable pictures of their baby, hoping to share the joy and create a friendly connection."
        ]
    },
    "mixer_social_DiscussExpandingTheFamily_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is initiating a friendly conversation with {target} to discuss the possibility of expanding their family."
        ]
    },
    "mixer_social_AskSimToPursueDreamJob_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is encouraging {target} to pursue their dream job, showing support and offering words of encouragement."
        ]
    },
    "mixer_social_Fight_targeted_mean_Ghost": {
        "pre_actions": [
            "{initiator} and {target} are getting into a heated battle, exchanging blows and insults. The tension is thickening as they are fighting to assert their dominance."
        ]
    },
    "mixer_Social_TalkRelationshipFears_Romance": {
        "pre_actions": [
            "{initiator} is opening up to {target} about their fears and concerns regarding their relationship."
        ]
    },
    "mixer_Social_Romance_AskAboutSexualOrientation": {
        "pre_actions": [
            "{initiator} is asking {target} about their romantic interests, in order to gain more insight into their potential compatibility."
        ]
    },
    "mixer_social_Targeted_Friendly_DiscussFears": {
        "pre_actions": [
            "{initiator} is approaching {target} in a friendly manner and is initiating a conversation about their fears."
        ]
    },
    "mixer_social_MeetInfant_Child_Greetings": {
        "pre_actions": [
            "{initiator} is walking up to {target} and warmly greeting them, eager to meet the newest addition to the family."
        ]
    },
    "mixer_Social_Friendly_FigureOutDifferences": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} to figure out their differences and understand them better."
        ]
    },
    "mixer_social_IsTheMoonCheese_targeted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} is playfully asking {target} if the moon is made of cheese, sparking a lighthearted conversation between the two."
        ]
    },
    "mixer_social_IsTheMoonABanana_targeted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} is playfully asking {target} if the moon is a banana, showing their friendly and childlike nature."
        ]
    },
    "mixer_social_IsTheMoonASponge_targeted_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} is playfully asking {target}, 'Do you think the Moon is a sponge?' in a friendly manner, engaging their imagination."
        ]
    },
    "mixer_social_WhereDidTheMoonGo_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator}, a friendly child Sim, is approaching {target} and innocently asking where the moon went."
        ]
    },
    "mixer_social_IsTheMoonAnEgg_Friendly_alwaysOn_child_skills": {
        "pre_actions": [
            "{initiator} is playfully asking {target} if the moon is actually an egg."
        ]
    },
    "mixer_Social_SexualOrientation_AskAboutWooHooInterests": {
        "pre_actions": [
            "{initiator} is asking {target} about their interests in WooHoo, in a social and curious manner."
        ]
    },
    "mixer_Social_SexualOrientation_AskToBeWooHooPartners": {
        "pre_actions": [
            "{initiator} is asking {target} if they would like to become WooHoo partners, hinting at a potential intimate relationship."
        ]
    },
    "mixer_Social_SexualOrientation_EndWooHooPartners": {
        "pre_actions": [
            "{initiator} and {target} are agreeing to end their WooHoo partnership, deciding to remain friends instead."
        ]
    },
    "mixer_social_SharePhoto": {
        "pre_actions": [
            "{initiator} is excitedly showing {target} some pictures from their phone."
        ]
    },
    "mixer_Social_Targeted_Friendly_Loyal_ConfessTrashTalk": {
        "pre_actions": [
            "{initiator} is approaching {target} to confess about some trash talk they have heard, expressing their loyalty to {target} and wanting to resolve the situation in a friendly manner."
        ]
    },
    "mixer_Social_Targeted_Romance_Loyal_ConfessCheating": {
        "pre_actions": [
            "{initiator} is bravely admitting to cheating on {target} in their relationship."
        ]
    },
    "mixer_Social_Targeted_Mean_Loyal_ConfrontAboutBullying": {
        "pre_actions": [
            "{initiator} is confronting {target} about their bullying behavior, showing their loyalty to the victim."
        ]
    },
    "mixer_Social_Targeted_Romance_Loyal_RebuildTrust": {
        "pre_actions": [
            "{initiator} is approaching {target} in an attempt to rebuild trust in their romantic relationship."
        ]
    },
    "mixer_social_Romance_HighScore_Loyal_ExpressDevotion": {
        "pre_actions": [
            "{initiator} is expressing their deep love and devotion to {target} in a romantic gesture."
        ]
    },
    "mixer_social_Hug_Friendly_Middlescore_NoMoodTest": {
        "pre_actions": [
            "{initiator} is warmly embracing {target} in a friendly hug."
        ]
    },
    "mixer_social_TalkAboutHerbalism_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about herbalism."
        ]
    },
    "mixer_social_EnthuseAboutHerbalism_targeted_Friendly_alwaysOn_trait": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their love for herbalism."
        ]
    },
    "mixer_social_LearnHerbalismRecipe_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is asking {target} if they can teach them a new herbalism recipe."
        ]
    },
    "mixer_social_DiscussAddingLog_targeted_friendly_situation_GP01": {
        "pre_actions": [
            "{initiator} is approaching {target} with the intention of discussing the possibility of adding a log to their property."
        ]
    },
    "mixer_social_ComplainAboutMosquitoes_targeted_Friendly_situation_GP01": {
        "pre_actions": [
            "{initiator} is approaching {target} and starting to complain about the annoying mosquitoes that have been bothering them."
        ]
    },
    "mixer_social_EnthuseAboutWildlifeEncounter_targeted_Friendly_situation_GP01": {
        "pre_actions": [
            "{initiator} is excitedly recounting a recent encounter with wildlife to {target}, hoping to share their enthusiasm."
        ]
    },
    "mixer_social_PhilosophizeAboutLife_targeted_Friendly_situation_GP01": {
        "pre_actions": [
            "{initiator} is engaging in a deep conversation with {target}, pondering the meaning of life."
        ]
    },
    "mixer_social_InsultFireBuildingSkills_targeted_mean_situation_GP01": {
        "pre_actions": [
            "{initiator} is rudely criticizing {target}'s ability to build fires."
        ]
    },
    "mixer_social_AskToStargaze_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is inviting {target} to stargaze together."
        ]
    },
    "mixer_Campfire_PlayWith": {
        "pre_actions": [
            "{initiator} is warming themselves by the campfire, enjoying some time alone."
        ]
    },
    "mixer_horseShoes_Discuss_Game": {
        "pre_actions": [
            "{initiator} and {target} are discussing the game of horse shoes."
        ]
    },
    "mixer_social_ShareAstronomyKnowledge_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is enthusiastically sharing their knowledge about astronomy with {target}, sparking an engaging conversation."
        ]
    },
    "mixer_social_Fight_targeted_mean_bear": {
        "pre_actions": [
            "{initiator} is challenging {target} to a wrestle, with a mean and bear-like demeanor."
        ]
    },
    "mixer_social_GossipAboutBear": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} to gossip about Bear."
        ]
    },
    "mixer_social_horseshoe_mean_heckle": {
        "pre_actions": [
            "{initiator} is using a mean approach and is starting to heckle {target} while playing horseshoes."
        ]
    },
    "mixer_social_horseshoe_friendly_cheer": {
        "pre_actions": [
            "{initiator} is cheering for {target} in a friendly and supportive manner."
        ]
    },
    "mixer_social_RantAboutBear": {
        "pre_actions": [
            "{initiator} is starting a passionate rant about an obnoxious bear to {target}."
        ]
    },
    "mixer_social_BearRoar": {
        "pre_actions": [
            "The bear is letting out a powerful roar, showcasing its dominance."
        ]
    },
    "mixer_social_BearRoar_Imitate": {
        "pre_actions": [
            "{initiator} is playfully imitating a bear's roar, causing {target} to be surprised and amused."
        ]
    },
    "mixer_social_AskAboutCamping_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking for information about camping."
        ]
    },
    "mixer_social_GiveHerbalismAdvice_Targeted_Friendly_AlwaysOn_skills": {
        "pre_actions": [
            "{initiator} is sharing some valuable herbalism tips with {target}, in a friendly and targeted way."
        ]
    },
    "mixer_social_MakeSmallTalk_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is engaging in casual conversation with {target}, trying to make small talk."
        ]
    },
    "mixer_social_AskPolitelyForInformation_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is approaching {target} and is politely asking them for information. It seems like {initiator} is trying to gather information in a fair and friendly manner."
        ]
    },
    "mixer_social_DiscussVictim_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is sitting down with {target} at the interrogation table to discuss the victim, taking on a good cop approach."
        ]
    },
    "mixer_social_DiscussPleaDeal_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is sitting {target} down at the interrogation table to discuss a potential plea deal, taking on the role of a good cop."
        ]
    },
    "mixer_social_AskAboutCrime_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is taking {target} to the interrogation table and asking about crime, playing the role of a good cop."
        ]
    },
    "mixer_social_TellPersonalStory_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is sitting down with {target} at the interrogation table and is starting to tell them a personal story, playing the role of a good cop."
        ]
    },
    "mixer_social_PretendToBeFriends_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is trying to act friendly and pretending to be friends with {target}, perhaps in an attempt to gather information or gain their trust."
        ]
    },
    "mixer_social_DescribePrisonHorrors_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is being strapped onto an interrogation table while a good cop is proceeding to describe the horrors of prison."
        ]
    },
    "mixer_social_MakeFalsePromises_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is sitting down with {target} at the interrogation table and trying to extract information by making false promises, playing the role of a good cop."
        ]
    },
    "mixer_social_OfferCandyBar_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is offering a candy bar to {target} while they are sitting at the interrogation table, taking on the role of the good cop."
        ]
    },
    "mixer_social_PromiseTastyMeal_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is promising {target} a tasty meal as they are sitting at the interrogation table, taking on the role of the good cop."
        ]
    },
    "mixer_social_PretendToCheckPhone_InterrogationTable_GoodCop": {
        "pre_actions": [
            "{initiator} is pretending to check their phone while secretly observing {target} for an interrogation. They are using a friendly approach, playing the good cop role."
        ]
    },
    "mixer_social_SlamCaseFile_InterrogationTable_BadCop_Emotion": {
        "pre_actions": [
            "{initiator} is forcefully slamming the case file onto the interrogation table, taking on a bad cop persona to intensify the emotional atmosphere."
        ]
    },
    "mixer_social_AskStressfulRiddles_InterrogationTable_BadCop_Emotion": {
        "pre_actions": [
            "{initiator} is putting {target} on the spot by asking them stressful riddles, putting them through an intense interrogation. The atmosphere is becoming tense and uncomfortable."
        ]
    },
    "mixer_social_Intimidate_InterrogationTable_BadCop_": {
        "pre_actions": [
            "{initiator} is using an intimidating tactic on {target} during an intense interrogation, playing the role of a bad cop."
        ]
    },
    "mixer_social_AskTrickQuestion_InterrogationTable_BadCop_Emotion": {
        "pre_actions": [
            "{initiator} is sneaking up on {target} and asking a trick question in a cunning attempt to interrogate them. {initiator} is adopting a Bad Cop persona, attempting to provoke a specific emotion from {target}."
        ]
    },
    "mixer_social_ThreatenWithSpiders_InterrogationTable_BadCop": {
        "pre_actions": [
            "{initiator} is menacingly waving a jar of spiders in front of {target}, using the interrogation table to play the role of a bad cop."
        ]
    },
    "mixer_social_ThreatenWithTickleTorture_InterrogationTable_BadCop": {
        "pre_actions": [
            "{initiator} is menacingly threatening {target} with the prospect of tickle torture, while the interrogation table is looming in the background. The atmosphere is being tense, giving off a strong 'bad cop' vibe."
        ]
    },
    "mixer_social_TellStoryAboutPrison_InterrogationTable_BadCop": {
        "pre_actions": [
            "{initiator} is sitting down at the interrogation table and is beginning to tell a gripping story about their experience in prison, while {target} is listening intently."
        ]
    },
    "mixer_social_GoOnTirade_InterrogationTable_BadCop": {
        "pre_actions": [
            "{initiator} is unleashing a furious tirade, interrogating {target} with a bad cop approach."
        ]
    },
    "mixer_social_PlayCrazyCop_InterrogationTable_BadCop": {
        "pre_actions": [
            "{initiator} is playing a game of Crazy Cop with {target} at the interrogation table, taking on the role of the Bad Cop."
        ]
    },
    "mixer_social_DemandAnswers_InterrogationTable_BadCop_Emotion": {
        "pre_actions": [
            "{initiator} is forcefully confronting {target} and demanding answers, using an interrogation table and adopting a bad cop demeanor."
        ]
    },
    "mixer_social_GlareColdly_InterrogationTable_BadCop": {
        "pre_actions": [
            "{initiator} is glaring coldly at {target} as part of an intense interrogation, taking on a bad cop approach."
        ]
    },
    "mixer_social_Ignore_InterrogationTable_BadCop": {
        "pre_actions": [
            "{initiator} is deliberately ignoring {target}, giving them the cold shoulder."
        ]
    },
    "mixer_social_DangleHandcuffs_InterrogationTable_BadCop": {
        "pre_actions": [
            "{initiator} is dangling a pair of handcuffs in front of {target}, implying an interrogation and taking on a bad cop demeanor."
        ]
    },
    "mixer_social_AskForBribe_InterrogationTable_BadCop": {
        "pre_actions": [
            "{initiator} is confronting {target} at the interrogation table, demanding a bribe."
        ]
    },
    "mixer_social_ShowCrimePictures_InterrogationTable_Evidence": {
        "pre_actions": [
            "{initiator} is showing {target} a collection of crime pictures on the interrogation table, presenting evidence for their investigation."
        ]
    },
    "mixer_social_ReviewCaseFile_InterrogationTable_Evidence": {
        "pre_actions": [
            "{initiator} is carefully examining the case file on the interrogation table, analyzing the gathered evidence."
        ]
    },
    "mixer_social_ShowWitnessStatement_InterrogationTable_Evidence": {
        "pre_actions": [
            "{initiator} is presenting a witness statement to {target} while sitting at the interrogation table, backed up by compelling evidence."
        ]
    },
    "mixer_social_BluffEvidence_InterrogationTable_Evidence": {
        "pre_actions": [
            "{initiator} is presenting the evidence to {target} in an attempt to bluff and manipulate them during the interrogation."
        ]
    },
    "mixer_social_RevealCallingCard_InterrogationTable_Evidence": {
        "pre_actions": [
            "{initiator} is using the Interrogation Table to reveal a calling card as evidence to {target}."
        ]
    },
    "mixer_social_ShowFingerprintEvidence_InterrogationTable_Evidence": {
        "pre_actions": [
            "{initiator} is presenting fingerprint evidence on the interrogation table to support their case."
        ]
    },
    "mixer_social_ReleaseInnocentSuspect_InterrogationTable_Special": {
        "pre_actions": [
            "{initiator} is releasing {target}, who is being found innocent after an interrogation at the special interrogation table."
        ]
    },
    "mixer_social_GetConfession_InterrogationTable_Special": {
        "pre_actions": [
            "{initiator} is taking {target} to the Interrogation Table in order to extract a confession."
        ]
    },
    "mixer_social_EndInterrogation_InterrogationTable_Special": {
        "pre_actions": [
            "{initiator} is finishing interrogating {target}, bringing an end to the intense questioning."
        ]
    },
    "mixer_social_Retail_Upsell_Targeted_Retail_HighScore": {
        "pre_actions": [
            "{initiator} is using their retail knowledge to recommend and endorse products to {target}, hoping to increase sales."
        ]
    },
    "mixer_social_Retail_Targeted_AnswerQuestions_Retail_MiddleScore": {
        "pre_actions": [
            "{initiator} is assisting {target} with their shopping by answering their questions about the retail products available."
        ]
    },
    "mixer_social_Retail_Targeted_PushCheaperItems_Retail_HighScore": {
        "pre_actions": [
            "{initiator} is offering {target} information about some cheaper items in the retail store."
        ]
    },
    "mixer_social_Retail_CloseTheDeal_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is engaging in a friendly and targeted conversation with {target} in order to close the deal in a retail setting."
        ]
    },
    "mixer_social_Retail_BegForSale_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is approaching {target} in a friendly manner and is begging them to make a sale in the retail store."
        ]
    },
    "mixer_social_Retail_PressureIntoSale_Targeted_Mean_EmotionSpecific": {
        "pre_actions": [
            "{initiator} is using targeted and forceful tactics to pressure {target} into making a purchase, displaying a mean behavior."
        ]
    },
    "mixer_social_DetermineBabyGender_targeted_Friendly_alwaysOn_ActiveCareer_Doctor": {
        "pre_actions": [
            "The active career doctor {initiator} is using their friendly attitude to determine the gender of {target}'s baby."
        ]
    },
    "mixer_social_CheckForFever_targeted_romance_alwaysOn_ActiveCareer_Doctor": {
        "pre_actions": [
            "{initiator}, being a doctor, is performing a check-up on {target} to assess their heat and symptoms of fever."
        ]
    },
    "mixer_social_GiveMedicalAdvice_targeted_Friendly_alwaysOn_ActiveCareer_Doctor": {
        "pre_actions": [
            "{initiator} is using their medical expertise to give {target} some friendly advice on their health."
        ]
    },
    "mixer_social_GiveBadMedicalAdvice_targeted_Mischief_alwaysOn_ActiveCareer_Doctor": {
        "pre_actions": [
            "{initiator} is playfully giving {target} some bad medical advice, causing them to question {initiator's} expertise as a doctor in their active career."
        ]
    },
    "mixer_social_Targeted_AnalyzePersonality_Friendly_AlwaysOn_Alien": {
        "pre_actions": [
            "{initiator} is taking a friendly approach and analyzing {target}'s personality, especially since {target} is an alien."
        ]
    },
    "mixer_social_SecretHandshake_Targeted_Friendly_AlwaysOn_Alien": {
        "pre_actions": [
            "{initiator} is initiating a secret handshake with {target}, showing their friendly and inclusive nature. Despite being an alien, {target} is happily accepting the gesture."
        ]
    },
    "mixer_social_Targeted_Empathize_Friendly_AlwaysOn_Alien": {
        "pre_actions": [
            "{initiator} is noticing that {target} seems upset and is approaching them with a friendly and empathetic demeanor, trying to understand and comfort them."
        ]
    },
    "mixer_social_Targeted_TalkAboutHome_Friendly_AlwaysOn_Alien": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, discussing their homes. Despite being an alien, {target} is seeming open and receptive."
        ]
    },
    "mixer_social_DiscussWork_Targeted_Friendly_AlwaysOn_coworkers": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} in order to discuss work-related matters, possibly because they are co-workers."
        ]
    },
    "mixer_social_GossipAboutCoworkers_Targeted_Friendly_AlwaysOn_coworkers": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, gossiping about their coworkers."
        ]
    },
    "mixer_social_ComplainAboutWork_Targeted_Friendly_AlwaysOn_coworkers": {
        "pre_actions": [
            "{initiator} is complaining to {target} about work, in a friendly and targeted manner, possibly discussing their shared frustrations with coworkers."
        ]
    },
    "mixer_social_Scientist_AccuseAlien": {
        "pre_actions": [
            "The scientist is accusing {target} of being an alien."
        ]
    },
    "mixer_social_ScareWithProbe_Targeted_Mischief_AlwaysOn_Alien": {
        "pre_actions": [
            "{initiator} is sneakily approaching {target} and scaring them with a probe, using their mischievous alien powers."
        ]
    },
    "mixer_hospitalExamBed_Exam_TakeTemp": {
        "pre_actions": [
            "{initiator} is placing {target} on the hospital examination bed and taking their temperature."
        ]
    },
    "mixer_hospitalExamBed_Exam_CheckEyes": {
        "pre_actions": [
            "{initiator} is leading {target} to the hospital exam bed to check their eyes."
        ]
    },
    "mixer_hospitalExamBed_Exam_CheckEar": {
        "pre_actions": [
            "{initiator} is lying down on the hospital examination bed and {target} is checking their ears to perform an examination."
        ]
    },
    "mixer_hospitalExamBed_Exam_ProbeChest": {
        "pre_actions": [
            "{initiator} is carefully scanning {target}'s body using an exam probe while they are lying on the hospital exam bed. The focus is being concentrated on the chest area."
        ]
    },
    "mixer_social_MemoryErase_Targeted_Mischief_AlwaysOn_Alien": {
        "pre_actions": [
            "{initiator} is using their advanced alien abilities to target {target}, erasing a specific memory from their mind."
        ]
    },
    "mixer_socials_AskForDNA_targeted_Friendly_alwaysOn_career": {
        "pre_actions": [
            "{initiator} is politely asking {target} for a DNA sample, as part of their career research."
        ]
    },
    "mixer_social_YellAtAngrily_InterrogationTable_SuspectActions": {
        "pre_actions": [
            "{initiator} is angrily yelling at {target} while they are both at the interrogation table, possibly due to {target}'s suspect actions."
        ]
    },
    "mixer_social_ShareMemory_InterrogationTable_SuspectActions": {
        "pre_actions": [
            "{initiator} is sharing a memory with {target}, hoping to gather information for an ongoing investigation."
        ]
    },
    "mixer_social_Decline_InterrogationTable_SuspectActions": {
        "pre_actions": [
            "{initiator} is firmly declining {target}'s request to be interrogated at the interrogation table, suspecting their actions."
        ]
    },
    "mixer_social_PlayMirrorGame_Targeted_Funny_AlwaysOn_clone": {
        "pre_actions": [
            "{initiator} is challenging {target} to a game where they are mimicking each other's actions in front of a mirror. The interaction is being carried out in a lighthearted manner and is full of laughter."
        ]
    },
    "mixer_social_DiscussSimilarities_Targeted_Friendly_AlwaysOn_clone": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, discussing their similarities."
        ]
    },
    "mixer_social_CallInferiorVersion_Targeted_Mean_AlwaysOn_clone": {
        "pre_actions": [
            "{initiator} is calling {target} an inferior version, in a mean and targeted manner, implying that {target} is a clone."
        ]
    },
    "mixer_social_InterrogationFinish_InterrogationTable_Special_hidden": {
        "pre_actions": [
            "{initiator} is concluding an intense interrogation at the specialized interrogation table with {target}."
        ]
    },
    "mixer_social_Freakout_InterrogationTable_SuspectActions": {
        "pre_actions": [
            "{initiator} is freaking out as they discover {target} interacting suspiciously with an interrogation table, suspecting their actions."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_DiscussHealth": {
        "pre_actions": [
            "{initiator} and {target} are sitting down on a hospital examination bed and having a discussion about general health."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_TakeSample": {
        "pre_actions": [
            "{initiator} is sitting down on the hospital examination bed and asking {target} to swab for a sample."
        ]
    },
    "mixer_hospitalExamBed_Seated_Social_Diagnosis_0_displayOnly": {
        "pre_actions": [
            "{initiator} is leading {target} to a hospital exam bed and they are both taking a seat. {initiator} is beginning to diagnose {target} for any illnesses."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_Diagnosis_BloatyHead": {
        "pre_actions": [
            "{target} is sitting on the hospital exam bed while {initiator} is examining them for a diagnosis of Bloaty Head."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_Diagnosis_BurningTummy": {
        "pre_actions": [
            "{initiator} is sitting on the hospital examination bed, getting diagnosed for their burning tummy."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_Diagnosis_GasAndGiggles": {
        "pre_actions": [
            "{initiator} and {target} are finding themselves in the hospital exam bed, both seated. The interaction is being filled with laughter as they are sharing silly jokes and engaging in light-hearted banter."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_Diagnosis_ItchyPlumbob": {
        "pre_actions": [
            "{initiator} is sitting on the hospital examination bed, experiencing an itchy plumbob. They are seeking a diagnosis from {target}."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_Diagnosis_LlamaFlu": {
        "pre_actions": [
            "{initiator} is sitting on the hospital exam bed while the doctor is diagnosing them with Llama Flu."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_Diagnosis_StarryEyes": {
        "pre_actions": [
            "{target} is sitting on the hospital examination bed while {initiator} is examining their starry eyes, trying to make a diagnosis."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_Diagnosis_SweatyShivers": {
        "pre_actions": [
            "{initiator} is sitting on the hospital examination bed, experiencing sweaty shivers, while waiting for a diagnosis."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_Diagnosis_TripleThreat": {
        "pre_actions": [
            "{initiator} is sitting on the hospital examination bed, while {target} is standing nearby. They are discussing the medical symptoms and making a diagnosis together, forming a \"Triple Threat\" team."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_Diagnosis_X_None": {
        "pre_actions": [
            "{initiator} and {target} are both staying healthy and are not requiring any medical examinations or treatment."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_StartGiveExam_thorough": {
        "pre_actions": [
            "{initiator} is carefully examining {target} while they are seated on the hospital examination bed, ensuring a thorough examination."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_StartGiveExam_quick": {
        "pre_actions": [
            "{initiator} is sitting down on the hospital examination bed and quickly starting to examine {target}."
        ]
    },
    "mixer_hospitalExamBed_Reclined_social_DiscussHealth": {
        "pre_actions": [
            "{initiator} and {target} are reclining on hospital exam beds, discussing their general health."
        ]
    },
    "mixer_hospitalExamBed_Reclined_social_GiveShot": {
        "pre_actions": [
            "{initiator} is laying {target} down on the hospital examination bed and administering a shot."
        ]
    },
    "mixer_hospitalExamBed_Reclined_social_DeliverTakeMeds": {
        "pre_actions": [
            "{initiator} is treating {target} with medication while they are laying on the hospital exam bed, reclined. {initiator} is delivering and {target} is taking the prescribed meds."
        ]
    },
    "mixer_hospitalExamBed_Reclined_social_DeliverEatFood": {
        "pre_actions": [
            "{initiator} is bringing a tray of food to the hospital exam bed where {target} is reclining, delivering a meal for them to eat."
        ]
    },
    "mixer_hospitalExamBed_Exam_CheckEar_hidden": {
        "pre_actions": [
            "{initiator} is inviting {target} to the hospital exam bed in order to check their ears."
        ]
    },
    "mixer_hospitalExamBed_Exam_CheckEyes_hidden": {
        "pre_actions": [
            "{initiator} is bringing {target} to the hospital examination bed to check their eyes."
        ]
    },
    "mixer_hospitalExamBed_Exam_ProbeChest_hidden": {
        "pre_actions": [
            "{initiator} is laying {target} down on the hospital exam bed and is beginning to scan their body with a probe, paying special attention to their chest."
        ]
    },
    "mixer_hospitalExamBed_Exam_TakeTemp_hidden": {
        "pre_actions": [
            "{initiator} is leading {target} to the hospital exam bed and is taking their temperature."
        ]
    },
    "mixer_social_CustomerIntroduction_greetings": {
        "pre_actions": [
            "{initiator} is warmly greeting the customer, extending a friendly welcome."
        ]
    },
    "mixer_social_Retail_SureSale_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is approaching {target} with a targeted and friendly approach, aiming to make a sure sale."
        ]
    },
    "mixer_social_AskAboutPriceRange_Targeted_Retail_AlwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking about their price range, indicating an interest in the retail items available."
        ]
    },
    "mixer_social_EnthuseAboutStore_Targeted_Retail_AlwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} all about the amazing items and deals at the store."
        ]
    },
    "mixer_social_DiscussShoppingPreferences_Targeted_Retail_AlwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target}, discussing their shopping preferences, potentially focusing on a specific retail store or brand."
        ]
    },
    "mixer_social_EnthuseAboutPrices_Targeted_Retail_MiddleScore": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target}, sharing their enthusiasm about prices at the retail store."
        ]
    },
    "mixer_social_SuggestOptions_Targeted_Retail_MiddleScore": {
        "pre_actions": [
            "{initiator} is suggesting various options for {target} to consider, specifically related to retail."
        ]
    },
    "mixer_social_GossipAboutOfficeRomance_Targeted_Friendly_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is engaging in a targeted and friendly conversation with {target}, gossiping about office romances."
        ]
    },
    "mixer_social_PraiseWorkEthic_Targeted_Friendly_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their strong work ethic, showing appreciation for their dedication and hard work in their active career."
        ]
    },
    "mixer_social_ComplainAboutWorkload_Targeted_Friendly_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is venting to {target} about their overwhelming workload, seeking empathy and understanding."
        ]
    },
    "mixer_social_BragAboutPromotion_Targeted_Friendly_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is excitedly approaching {target} and bragging about their recent promotion in their active career, aiming to impress them with their achievements."
        ]
    },
    "mixer_social_CongratulateOnPromotion_Targeted_Friendly_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is approaching {target} with a smile and is offering heartfelt congratulations on their recent promotion."
        ]
    },
    "mixer_social_AskAboutSalary_Targeted_Friendly_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking about their salary, in a friendly and non-intrusive manner. This interaction is relating to their active career."
        ]
    },
    "mixer_social_DiscussCase_Targeted_Friendly_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is approaching {target} to discuss a case related to their active career, in a friendly and targeted manner."
        ]
    },
    "mixer_Social_EnthuseAboutSolvingCase_targeted_Friendly_alwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their latest case and how they are determined to solve it."
        ]
    },
    "mixer_Social_EnthuseAboutInventions_targeted_Friendly_alwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their latest inventions, discussing their shared interest in innovative technology. They are bonding over their passion for their active careers."
        ]
    },
    "mixer_Social_EnthuseAboutDeliveringBaby_targeted_Friendly_alwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is enthusiastically talking to {target} about their experience delivering a baby, showing support and excitement for {target}'s active career."
        ]
    },
    "mixer_social_InsultWorkEthic_Targeted_Mean_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is targeting {target} by making a mean comment about their work ethic, possibly due to their active career."
        ]
    },
    "mixer_social_SpoilLatestEpisode_Targeted_Mean_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is maliciously spoiling the latest episode for {target}, possibly out of spite or to provoke a reaction. However, it's worth noting that {initiator} might be having a career or hobby related to being active in the entertainment industry."
        ]
    },
    "mixer_social_PretendToFire_Targeted_Mean_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is pretending to fire {target}, as a mean-spirited act. This interaction is being influenced by {initiator}'s active career."
        ]
    },
    "mixer_social_FlirtCovertly_Targeted_Romance_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is flirting with {target} in a subtle and discreet manner, hoping to spark some romantic interest. This interaction is being influenced by the fact that {initiator} is having an active career."
        ]
    },
    "mixer_social_JokeAboutCoworkers_Targeted_Funny_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is telling a joke about co-workers to {target}, making them laugh."
        ]
    },
    "mixer_social_TellNSFWJoke_Targeted_Funny_AlwaysOn_ActiveCareer": {
        "pre_actions": [
            "{initiator} is telling a targeted NSFW joke to {target}, adding some humor to their interaction. This may be related to their ongoing career."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_TreatPatient_display": {
        "pre_actions": [
            "{initiator} is treating {target}, who is seated on the hospital examination bed."
        ]
    },
    "mixer_social_Targeted_AskAboutParty_Friendly_AlwaysOn_Alien": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking about the party, in a friendly and curious manner. {initiator} is not noticing that {target} is an alien."
        ]
    },
    "mixer_social_Clone_Greeting": {
        "pre_actions": [
            "{initiator} is greeting their clone self with a friendly hello."
        ]
    },
    "mixer_social_DebateMedicalTheory_targeted_Friendly_alwaysOn_activeCareer_doctor": {
        "pre_actions": [
            "{initiator} is engaging in a friendly debate with {target} regarding medical theory, as part of their active career as a doctor."
        ]
    },
    "mixer_hospitalExamBed_Seated_social_TalkAboutHealthcare": {
        "pre_actions": [
            "{initiator} and {target} are sitting on a hospital exam bed and discussing healthcare."
        ]
    },
    "mixer_hospitalExamBed_Reclined_social_TalkAboutHealthcare": {
        "pre_actions": [
            "{initiator} and {target} are having a conversation while reclining on the hospital examination bed, discussing healthcare."
        ]
    },
    "mixer_hospitalExamBed_Doctor_TransferPatientCase": {
        "pre_actions": [
            "{initiator}, a doctor, is transferring a patient's case to {target} at the hospital exam bed."
        ]
    },
    "mixer_yogaMat_GreetingPose": {
        "pre_actions": [
            "{initiator} is stretching out on their yoga mat in a greeting pose, welcoming {target}."
        ]
    },
    "mixer_yogaMat_HalfMoonPose": {
        "pre_actions": [
            "{initiator} is gracefully standing on one leg on the yoga mat, perfectly executing the Half Moon Pose."
        ]
    },
    "mixer_yogaMat_DownwardFacingDog": {
        "pre_actions": [
            "{initiator} is gracefully stretching into a downward facing dog pose on the yoga mat."
        ]
    },
    "mixer_yogaMat_TrianglePose": {
        "pre_actions": [
            "{initiator} is finding a yoga mat and performing the Triangle Pose."
        ]
    },
    "mixer_yogaMat_TreePose": {
        "pre_actions": [
            "{initiator} is striking a balanced Tree Pose on the yoga mat."
        ]
    },
    "mixer_yogaMat_DancePose": {
        "pre_actions": [
            "{initiator} is striking a Lord of the Dance Pose on their yoga mat."
        ]
    },
    "mixer_yogaMat_BridgePose": {
        "pre_actions": [
            "{initiator} is performing the Bridge Pose on the yoga mat."
        ]
    },
    "mixer_yogaMat_Corpse": {
        "pre_actions": [
            "{initiator} is lying down on the yoga mat in a corpse pose."
        ]
    },
    "mixer_yogaMat_BridgePose_Practice": {
        "pre_actions": [
            "{initiator} is positioning themselves on a yoga mat and starting to practice the Bridge Pose."
        ]
    },
    "mixer_yogaMat_DancePose_Practice": {
        "pre_actions": [
            "{initiator} is gracefully striking the Lord of the Dance pose on their yoga mat, practicing their dance moves."
        ]
    },
    "mixer_yogaMat_DownwardFacingDog_Practice": {
        "pre_actions": [
            "{initiator} is getting on a yoga Mat and starting to practice the Downward Facing Dog pose."
        ]
    },
    "mixer_yogaMat_HalfMoonPose_Practice": {
        "pre_actions": [
            "{initiator} is gracefully moving into the Half Moon Pose on the yoga mat, focusing on their practice."
        ]
    },
    "mixer_yogaMat_TreePose_Practice": {
        "pre_actions": [
            "{initiator} is gracefully balancing on one leg in the Tree Pose on a yoga mat, practicing their yoga skills."
        ]
    },
    "mixer_yogaMat_TrianglePose_Practice": {
        "pre_actions": [
            "{initiator} is demonstrating the Triangle Pose on their yoga yoga mat, practicing their yoga skills."
        ]
    },
    "mixer_social_GiveMassage_Swedish_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is offering to give {target} a soothing Swedish massage as a friendly gesture."
        ]
    },
    "mixer_social_GiveMassage_DeepTissue_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is offering a friendly deep tissue massage to {target}."
        ]
    },
    "mixer_social_GiveMassage_StoneMassage_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is offering to give {target} a relaxing stone massage."
        ]
    },
    "mixer_social_GiveMassage_SportsMassage_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is giving {target} a friendly sports massage."
        ]
    },
    "mixer_social_GiveMassage_Fertility_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is giving {target} a fertility massage to help increase their chances of getting pregnant."
        ]
    },
    "mixer_social_GiveMassage_Aromatherapy_YlangYlang_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is giving {target} a relaxing aromatherapy massage using Ylang Ylang oil."
        ]
    },
    "mixer_social_GiveMassage_Aromatherapy_Mint_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is giving {target} a relaxing aromatherapy massage using mint and rosemary oils."
        ]
    },
    "mixer_social_GiveMassage_Aromatherapy_LotusBlossom_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is giving {target} a soothing aromatherapy massage using Lotus Blossom oil."
        ]
    },
    "mixer_social_GiveMassage_Aromatherapy_Lavender_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is giving {target} a soothing aromatherapy massage using lavender oil."
        ]
    },
    "mixer_social_AskForMassage_Swedish_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they can give them a Swedish massage."
        ]
    },
    "mixer_social_AskForMassage_DeepTissue_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they would be willing to give them a deep tissue massage."
        ]
    },
    "mixer_social_AskForMassage_SportsMassage_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they could give them a sports massage."
        ]
    },
    "mixer_social_AskForMassage_StoneMassage_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} if they would like a stone massage."
        ]
    },
    "mixer_social_AskForMassage_Fertility_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they would be willing to give them a fertility massage."
        ]
    },
    "mixer_social_AskForMassage_Aromatherapy_Ylang_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they would be willing to give them a relaxing Ylang Ylang aromatherapy massage."
        ]
    },
    "mixer_social_AskForMassage_Aromatherapy_Mint_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} if they can have a Mint and Rosemary Aromatherapy Massage."
        ]
    },
    "mixer_social_AskForMassage_Aromatherapy_Lavender_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they could give them a lavender aromatherapy massage."
        ]
    },
    "mixer_social_AskForMassage_Aromatherapy_LotusBlossom_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they could give them a Lotus Blossom Aromatherapy Massage."
        ]
    },
    "mixer_social_ShareDetoxSecrets_targeted_Friendly_alwaysOn_skill": {
        "pre_actions": [
            "{initiator} is sharing their detox secrets with {target}."
        ]
    },
    "mixer_social_OfferMentalRelaxationTips_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is offering {target} some tips on how to relax mentally."
        ]
    },
    "mixer_social_DiscussCognitiveFocusingMethods_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in a friendly discussion with {target} about cognitive focusing methods."
        ]
    },
    "mixer_social_SuggestVisualizationTechniques_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is kindly suggesting some visualization techniques to {target} that could help them."
        ]
    },
    "mixer_social_RecommendSelfEsteemExercises_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is suggesting some self-esteem exercises to {target} in a friendly manner."
        ]
    },
    "mixer_social_CompareEssentialOils_Targeted_Friendly_AlwaysOn_MassageTherapist": {
        "pre_actions": [
            "{initiator}, a massage therapist, is engaging in a friendly conversation with {target} to compare different essential oils."
        ]
    },
    "mixer_social_DiscussPressurePoints_Targeted_Friendly_AlwaysOn_MassageTherapist": {
        "pre_actions": [
            "{initiator} is engaging in a targeted and friendly conversation with {target}, discussing pressure points. It seems like {initiator} may be a massage therapist."
        ]
    },
    "mixer_social_AskAboutMassageBenefits_Targeted_Friendly_AlwaysOn_MassageTherapist": {
        "pre_actions": [
            "{initiator} is approaching {target}, a massage therapist, and asking about the benefits of getting a massage."
        ]
    },
    "mixer_social_AskForFlexibilityTips_Targeted_Friendly_AlwaysOn_YogaInstructor": {
        "pre_actions": [
            "{initiator} is approaching {target}, a yoga instructor, and asking for some tips on how to improve flexibility."
        ]
    },
    "mixer_social_ChatAboutYogaClass_Targeted_Friendly_AlwaysOn_Yoga": {
        "pre_actions": [
            "{initiator} is initiating a friendly conversation with {target}, specifically about their yoga class."
        ]
    },
    "mixer_social_ComplimentYogaPants_targeted_romance_alwaysOn_YogaInstructor": {
        "pre_actions": [
            "{initiator} is complimenting {target}'s yoga pants, showing romantic interest in the yoga instructor."
        ]
    },
    "mixer_social_GetAMassage_DeepTissue_targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is requesting a deep tissue massage from {target}, seeking relief and relaxation."
        ]
    },
    "mixer_Social_RequestHandMassage_Targeted_Friendly_AlwaysOn_Reflexologist": {
        "pre_actions": [
            "{initiator} is approaching {target}, a skilled reflexologist, and is politely requesting a hand massage."
        ]
    },
    "mixer_social_GetAMassage_SwedishMassage_targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is requesting a Swedish massage from {target} in a friendly manner."
        ]
    },
    "mixer_social_GetAMassage_SportsMassage_targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is requesting a sports massage from {target}, seeking their friendly and skillful touch."
        ]
    },
    "mixer_social_GetAMassage_StoneMassage_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is scheduling a targeted stone massage for {target} in order to help them relax and unwind."
        ]
    },
    "mixer_social_GetAMassage_FertilityMassage_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} if they would like to get a fertility massage, a targeted and friendly interaction to promote fertility."
        ]
    },
    "mixer_social_GetAMassage_Aromatherapy_Mint_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is inviting {target} to receive a relaxing aromatherapy massage using mint and rosemary scented oils."
        ]
    },
    "mixer_social_GetAMassage_Aromatherapy_YlangYlang_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is enjoying a Ylang Ylang aromatherapy massage from {target}."
        ]
    },
    "mixer_social_GetAMassage_Aromatherapy_Lavender_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is inviting {target} to come over and receive a relaxing lavender aromatherapy massage."
        ]
    },
    "mixer_social_GetAMassage_Aromatherapy_LotusBlossom_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is requesting a Lotus Blossom Aromatherapy Massage from {target} in a friendly manner."
        ]
    },
    "mixer_social_DiscussReflexologyTheory_targeted_Friendly_alwaysOn_reflexologist": {
        "pre_actions": [
            "{initiator} is engaging in a friendly discussion about reflexology theory with {target}, a fellow reflexologist."
        ]
    },
    "mixer_social_AskAboutReflexPoints_Targeted_Friendly_alwaysOn_reflexologist": {
        "pre_actions": [
            "{initiator} is approaching {target}, a reflexologist, and is asking them about reflex points in a friendly manner."
        ]
    },
    "mixer_social_WooHooInSteamRoom_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are unable to resist the steamy atmosphere of the sauna and are deciding to engage in a passionate WooHoo session."
        ]
    },
    "mixer_social_TryForBabyInSteamRoom_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into the sauna for some private time and are trying for a baby."
        ]
    },
    "mixer_Social_RequestFootMassage_Targeted_Friendly_AlwaysOn_Reflexologist": {
        "pre_actions": [
            "{initiator} is kindly asking {target} for a foot massage, knowing that they have skills in reflexology."
        ]
    },
    "mixer_yogaMat_WarriorPose": {
        "pre_actions": [
            "{initiator} is striking a Warrior Pose on the yoga mat."
        ]
    },
    "mixer_yogaMat_WarriorPose_Practice": {
        "pre_actions": [
            "{initiator} is striking a Warrior Pose on their yoga mat, practicing their yoga moves."
        ]
    },
    "mixer_yogaMat_BoatPose": {
        "pre_actions": [
            "{initiator} is demonstrating the Boat Pose on a yoga mat."
        ]
    },
    "mixer_yogaMat_BoatPose_Practice": {
        "pre_actions": [
            "{initiator} is getting onto a yoga mat and starting to practice the Boat Pose."
        ]
    },
    "mixer_yogaMat_HandStand": {
        "pre_actions": [
            "{initiator} is showing off their impressive handstand skills on a yoga mat."
        ]
    },
    "mixer_yogaMat_HandStand_Practice": {
        "pre_actions": [
            "{initiator} is setting up a yoga mat and beginning to practice handstands."
        ]
    },
    "mixer_Social_AskForHandMassage_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} for a hand massage, hoping they can provide some relaxation."
        ]
    },
    "mixer_Social_AskForFootMassage_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they would be willing to give them a foot massage."
        ]
    },
    "mixer_YogaClass_ClassMember_CorpsePose": {
        "pre_actions": [
            "{initiator} is lying down on the yoga mat and is beginning to perform the Corpse Pose during the yoga class, alongside {target} who is also participating in the class."
        ]
    },
    "mixer_Social_OfferFootMassage_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is kindly offering {target} a foot massage as a friendly gesture."
        ]
    },
    "mixer_Social_OfferHandMassage_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is offering a hand massage to {target}, aiming to provide relaxation and show kindness."
        ]
    },
    "mixer_YogaMat_Corpse_SleepExit": {
        "pre_actions": [
            "{initiator} is lying down on a YogaMat in the Corpse Pose, appearing to be asleep."
        ]
    },
    "mixer_YogaMat_Corpse_NormalExit": {
        "pre_actions": [
            "{initiator} is lying down in the Corpse Pose on a Yoga Mat and peacefully exiting the pose."
        ]
    },
    "mixer_YogaMat_Corpse_NormalExit_YogaClass": {
        "pre_actions": [
            "{initiator} is lying down on the YogaMat in a Corpse Pose, as part of a normal exit from a Yoga Class."
        ]
    },
    "mixer_YogaMat_Corpse_SleepExit_YogaClass": {
        "pre_actions": [
            "{initiator} is lying down in the Corpse Pose on the Yoga Mat, appearing as if they are peacefully asleep. They have finished their Yoga Class and are getting ready to exit the session."
        ]
    },
    "mixer_YogaClass_Instructor_CorpsePose": {
        "pre_actions": [
            "{initiator} is guiding the yoga class and instructing {target} to get into the Corpse Pose."
        ]
    },
    "mixer_YogaMat_Corpse_NormalExit_YogaClass_Mirrored": {
        "pre_actions": [
            "{initiator} is lying down on a yoga mat in a corpse pose during a normal exit from a yoga class. The yoga mat is being mirrored."
        ]
    },
    "mixer_YogaMat_Corpse_SleepExit_YogaClass_Mirrored": {
        "pre_actions": [
            "{initiator} is lying down in the Corpse Pose on a Yoga Mat, appearing as if they are sleeping. They are exiting the Yoga Class with a mirrored reflection, feeling relaxed and rejuvenated."
        ]
    },
    "mixer_Social_AskForManicure_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they can do their manicure."
        ]
    },
    "mixer_Social_AskForPedicure_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they would be willing to give them a pedicure."
        ]
    },
    "mixer_Social_OfferManicure_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is offering to give {target} a manicure, in a friendly and targeted social interaction."
        ]
    },
    "mixer_Social_OfferPedicure_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is offering {target} a pedicure as a friendly gesture."
        ]
    },
    "mixer_social_BragAboutNails": {
        "pre_actions": [
            "{initiator} is excitedly showing off their beautifully manicured nails to {target}, bragging about how amazing they look."
        ]
    },
    "mixer_social_ComplainAboutNails": {
        "pre_actions": [
            "{initiator} is being irritated with the state of their nails and is beginning to complain to {target} about them."
        ]
    },
    "mixer_social_RequestManicure_Targeted_Friendly_AlwaysOn_Reflexologist": {
        "pre_actions": [
            "{initiator} is asking {target} in a friendly manner if they would be willing to give them a manicure, knowing that {target} is a skilled reflexologist."
        ]
    },
    "mixer_social_RequestPedicure_Targeted_Friendly_AlwaysOn_Reflexologist": {
        "pre_actions": [
            "{initiator} is kindly asking {target} if they can give them a pedicure, as they are a skilled reflexologist."
        ]
    },
    "mixer_social_HighMaintenance_ComplainAboutDailyStruggles_Trait": {
        "pre_actions": [
            "{initiator} is complaining to {target} about the uncomfortable seats, due to their High Maintenance trait and tendency to complain about daily struggles."
        ]
    },
    "mixer_social_HighMaintenance_ShareCatharsisMoment_Trait": {
        "pre_actions": [
            "{initiator}, being a High Maintenance Sim, is sharing a cathartic moment with {target}."
        ]
    },
    "mixer_social_FacialMask_OfferMask": {
        "pre_actions": [
            "{initiator} is kindly offering to apply a facial mask to {target}'s face for a pampering session."
        ]
    },
    "mixer_social_ChillingTouch_targeted_mischief_skills": {
        "pre_actions": [
            "{initiator} is mischievously using a chilling touch on {target}, giving them a cold, spooky sensation."
        ]
    },
    "mixer_social_AskforPartyTreat_targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they could please give them a party treat."
        ]
    },
    "mixer_social_RequestSimCarvePumpkin_targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is kindly asking {target} if they would be willing to carve a pumpkin for them."
        ]
    },
    "mixer_foosball_DiscussGame": {
        "pre_actions": [
            "{initiator} and {target} are discussing their recent foosball game, sharing strategies and highlights."
        ]
    },
    "mixer_Social_Clubs_NT_InviteToClub": {
        "pre_actions": [
            "{initiator} is inviting {target} to join the {0.String} club."
        ]
    },
    "mixer_Social_Clubs_NT_AskToJoin": {
        "pre_actions": [
            "{initiator} is asking {target} if they can join the {0.String} club."
        ]
    },
    "mixer_Social_Clubs_NT_TalkAbout": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a conversation about {0.String}."
        ]
    },
    "mixer_Social_Clubs_NT_PraiseClubLeader": {
        "pre_actions": [
            "{initiator} is complimenting {target}'s leadership skills and is praising them for their role as the leader of the club."
        ]
    },
    "mixer_Social_Clubs_NT_ComplainAboutClubLeader": {
        "pre_actions": [
            "{initiator} is approaching {target} to express their dissatisfaction about the current leader of the {0.String} club."
        ]
    },
    "mixer_Social_Clubs_NT_OverthrowClubLeader": {
        "pre_actions": [
            "{initiator} is gathering members of the Overthrow Club to plot and overthrow {target}'s leader."
        ]
    },
    "mixer_Social_Clubs_NT_ConvinceLeaderToStepDown": {
        "pre_actions": [
            "{initiator} is using their social influence within the {0.String} club to convince {target} to step down as their leader."
        ]
    },
    "mixer_social_WooHoo_targeted_romance_transition_Closet": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into a closet together for a steamy and intimate encounter."
        ]
    },
    "mixer_social_TryForBaby_targeted_romance_transition_Closet": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into a closet for a private moment and trying for a baby together."
        ]
    },
    "mixer_social_ScoldClubMember_Targeted_Mean_AlwaysOn": {
        "pre_actions": [
            "{initiator} is scolding {target}, who is a fellow club member, for breaking the rules."
        ]
    },
    "mixer_social_GoingOutSocials_AskAboutAnotherSim": {
        "pre_actions": [
            "{initiator} is asking {target} about another Sim, wanting to know more information about them."
        ]
    },
    "mixer_social_Closet_MakeOut_targeted_romance_highScore": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into a closet and passionately making out."
        ]
    },
    "mixer_social_targeted_friendly_MiddleScore_SeeOutfit_Everyday": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their everyday outfit, sparking a friendly conversation."
        ]
    },
    "mixer_social_targeted_friendly_MiddleScore_SeeOutfit_Formal": {
        "pre_actions": [
            "{initiator} is complimenting {target}'s formal outfit and engaging in a friendly conversation."
        ]
    },
    "mixer_social_targeted_friendly_MiddleScore_SeeOutfit_Athletic": {
        "pre_actions": [
            "{initiator} is complimenting {target}'s athletic physique and asking to see their workout outfit."
        ]
    },
    "mixer_social_targeted_friendly_MiddleScore_SeeOutfit_Swim": {
        "pre_actions": [
            "{initiator} is complimenting {target}'s swimwear and suggesting they go swimming together."
        ]
    },
    "mixer_social_targeted_friendly_MiddleScore_SeeOutfit_Sleep": {
        "pre_actions": [
            "{initiator} is complimenting {target}'s sleepwear and is suggesting having a cozy night in together."
        ]
    },
    "mixer_social_targeted_friendly_MiddleScore_SeeOutfit_Party": {
        "pre_actions": [
            "{initiator} is inviting {target} to a party and is suggesting they try on different outfits together."
        ]
    },
    "mixer_social_DiscussDJMusic_targeted_Friendly_alwaysOn_STC": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a friendly conversation about DJ techniques and music."
        ]
    },
    "mixer_Social_Clubs_NT_AskToStartClubGathering": {
        "pre_actions": [
            "{initiator} is asking {target} to start a social club gathering."
        ]
    },
    "mixer_Social_Clubs_NT_DiscussLeadersFeelings": {
        "pre_actions": [
            "{initiator} and {target} are being part of the same social club and are engaging in a discussion about their feelings regarding their leader."
        ]
    },
    "mixer_social_GoingOutSocials_ExchangeNumbers": {
        "pre_actions": [
            "{initiator} is asking {target} for their phone number, suggesting they should be exchanging numbers to stay in touch."
        ]
    },
    "mixer_Social_Clubs_NT_QuitClub": {
        "pre_actions": [
            "{initiator} is deciding to quit the club, in order to pursue other interests."
        ]
    },
    "mixer_Social_Clubs_NT_KickOut": {
        "pre_actions": [
            "{initiator} is using their authority in the club to kick {target} out."
        ]
    },
    "mixer_social_AskAboutClubs_Targeted_Friendly_AlwaysOn_Clubs": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking them about clubs, hoping to engage in a friendly conversation and learn more about their interests."
        ]
    },
    "mixer_social_targeted_TalkAboutParty_Trait_DanceMachine": {
        "pre_actions": [
            "{initiator} is approaching {target} and enthusiastically talking about the latest party, knowing that {target} is also enjoying dancing thanks to their Dance Machine trait."
        ]
    },
    "mixer_Social_Clubs_NT_ConviceToLeaveClub": {
        "pre_actions": [
            "{initiator} is trying to convince {target} to quit the {0.String} social club."
        ]
    },
    "mixer_Social_Clubs_NT_ResignFromClub": {
        "pre_actions": [
            "{initiator} is deciding to resign from the {0.String} social club, no longer wanting to be a part of it."
        ]
    },
    "mixer_social_InsiderTrait_TellInsiderStory_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} is sharing an insider story with {target}, creating a friendly and engaging conversation."
        ]
    },
    "mixer_DJBooth_GiveTipToPlayer": {
        "pre_actions": [
            "{initiator} is approaching the DJ booth and is giving a tip to {target} who is the DJ."
        ]
    },
    "mixer_social_DiscussDanceTechnique_targeted_Friendly_alwaysOn_STC": {
        "pre_actions": [
            "{initiator} is approaching {target} to discuss dance techniques in a friendly manner."
        ]
    },
    "mixer_Social_Dartboard_DiscussGame_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is inviting {target} to discuss the game while playing a friendly game of darts."
        ]
    },
    "mixer_social_targeted_friendly_MiddleScore_SeeOutfit_ColdOutfit": {
        "pre_actions": [
            "{initiator} is noticing that {target} is not dressed appropriately for the cold weather. In a friendly manner, {initiator} is suggesting that {target} should consider changing into a warmer outfit."
        ]
    },
    "mixer_social_targeted_friendly_MiddleScore_SeeOutfit_HotOutfit": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their hot weather outfit, starting a friendly conversation."
        ]
    },
    "mixer_socials_EnthuseAboutMeal_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator} is enthusiastically talking to {target} about a delicious meal, engaging in a friendly and targeted conversation."
        ]
    },
    "mixer_socials_ComplainAboutDish_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator} is approaching {target} and complaining about a dish they had at a restaurant, sparking a friendly conversation between them."
        ]
    },
    "mixer_socials_DiscussFoodFlavors_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator} is engaging in a friendly discussion with {target} about different food flavors."
        ]
    },
    "mixer_social_SitIntimate_FeedABite_targeted_romance_alwaysOn": {
        "pre_actions": [
            "{initiator} is sitting closely next to {target} and is feeding them a bite of food, creating an intimate and romantic moment."
        ]
    },
    "mixer_socials_EnthuseAboutExperimentalFood_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their experimental meal, hoping to share their passion for unique and delicious food."
        ]
    },
    "mixer_socials_ComplainAboutExperimentalFood_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator} is targeting {target} and is expressing their dissatisfaction with the experimental dish they were served during the meal in a friendly manner."
        ]
    },
    "mixer_socials_DiscussExperimentalFood_Targeted_Friendly_AlwaysOn_DiningSocials": {
        "pre_actions": [
            "{initiator} and {target} are sitting down to discuss experimental food flavors, sharing their thoughts and opinions in a friendly and engaging conversation."
        ]
    },
    "mixer_social_ComplainAboutFoodPoisoning_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} and complaining about experiencing food poisoning, hoping for sympathy and understanding."
        ]
    },
    "mixer_social_BragAboutFoodPoisoning_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} about surviving food poisoning, eager to impress them with their resilience and strength."
        ]
    },
    "mixer_social_AskToDeliverCompliment_Targeted_Friendly_AlwaysOn_WaitStaff": {
        "pre_actions": [
            "{initiator} is politely asking {target} if they can deliver a compliment to the wait staff."
        ]
    },
    "mixer_social_AskToDeliverInsult_Targeted_Friendly_AlwaysOn_WaitStaf": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking them to deliver an insult to someone, but in a friendly and lighthearted manner."
        ]
    },
    "mixer_social_ChatAboutActors_targeted_Friendly_Movie_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly conversation about their favorite actors and movies."
        ]
    },
    "mixer_socials_EnthuseAboutMovie_targeted_Friendly_Movie_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about a movie they recently watched and enjoyed."
        ]
    },
    "mixer_socials_AskQuestionAboutPlot_targeted_Friendly_Movie_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, asking them about the plot of a movie."
        ]
    },
    "mixer_socials_DiscussScene_targeted_Friendly_Movie_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is initiating a friendly conversation with {target} to discuss a movie scene."
        ]
    },
    "mixer_socials_DeclareFavoriteGenre_targeted_Friendly_Movie_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} their favorite movie genre, hoping to spark a conversation about their shared interest in movies."
        ]
    },
    "mixer_socials_SpreadFakeSpoilers_targeted_Mischief_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is mischievously spreading fake spoilers to {target} during their conversation."
        ]
    },
    "mixer_socials_ComplainAboutActor_targeted_Friendly_Movie_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is approaching {target} and starting a friendly conversation about a movie, expressing their disappointment with the performance of a certain actor."
        ]
    },
    "mixer_socials_ComplainAboutDirector_targeted_Friendly_Movie_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is approaching {target} and starting a friendly conversation, complaining about the director of a movie they are watching together."
        ]
    },
    "mixer_social_UltimatePickUp_targeted_romance_AlwaysOn": {
        "pre_actions": [
            "{initiator} is confidently approaching {target} and using the ultimate pick-up line to spark a romantic connection."
        ]
    },
    "mixer_social_UltimatePickUp_targeted_romance_AlwaysOn_teen": {
        "pre_actions": [
            "{initiator} is confidently approaching {target} and using the ultimate pick-up line, attempting to spark a romantic connection between them."
        ]
    },
    "mixer_social_Blackmail_targeted_mean_alwaysOn": {
        "pre_actions": [
            "{initiator} is threatening {target} with some incriminating information, in an attempt to control or manipulate them."
        ]
    },
    "mixer_social_AskToPlayInFountain_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} if they want to play in the fountain together."
        ]
    },
    "mixer_socials_AskToTrade_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking if they would like to trade Voidcritters."
        ]
    },
    "mixer_socials_AskToTrade_FromPicker_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is initiating a friendly conversation with {target} and is asking if they would be interested in trading Voidcritters."
        ]
    },
    "mixer_social_PraiseVampireLifestyle_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their vampire lifestyle, showing sincere admiration."
        ]
    },
    "mixer_social_EnthuseAboutVampires_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about vampires, expressing their enthusiasm for the topic."
        ]
    },
    "mixer_social_ConfessFearOfVampires_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is reaching out to {target} and confessing their fear of vampires, hoping to receive support and understanding."
        ]
    },
    "mixer_social_DebateExistenceOfVampires_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is initiating a friendly debate with {target} about the existence of vampires."
        ]
    },
    "mixer_social_InsultFangSize_Targeted_Mean_AlwaysOn_Vampire": {
        "pre_actions": [
            "{initiator} is rudely insulting {target}'s fang size, aiming to be mean and hurtful."
        ]
    },
    "mixer_social_DeclareEternalLove_Targeted_Romance_HighScore": {
        "pre_actions": [
            "{initiator} is declaring eternal love to {target}, expressing their deep romantic feelings."
        ]
    },
    "mixer_social_DiscussPlasmaFlavors_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, discussing different flavors of plasma."
        ]
    },
    "mixer_social_GossipAboutVampires_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly sharing some juicy gossip about ancient vampires with {target}, sparking a friendly conversation."
        ]
    },
    "mixer_social_BroodAboutBeingAVampire_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is confiding in {target} about the struggles of being a vampire, seeking friendly support."
        ]
    },
    "mixer_social_OfferAdviceOnVampireLife_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is offering {target} advice on how to navigate the vampire life, sharing tips and experiences."
        ]
    },
    "mixer_social_MockLackOfPower_Targeted_Mean_AlwaysOn": {
        "pre_actions": [
            "{initiator} is making fun of {target}'s lack of power, being mean-spirited."
        ]
    },
    "mixer_social_LectureAboutSunlight_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is delivering a targeted and friendly lecture to {target} about the importance of sunlight."
        ]
    },
    "mixer_social_ShareAncientLore_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, sharing ancient lore and stories."
        ]
    },
    "mixer_social_VampireCreation_AskToTurn": {
        "pre_actions": [
            "{initiator} is asking {target} if they would like to be turned into a vampire."
        ]
    },
    "mixer_social_AskForAdviceOnBitingTechnique_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} in a friendly manner and is asking for advice on improving their biting technique."
        ]
    },
    "mixer_social_VampireCreation_OfferToTurn": {
        "pre_actions": [
            "{initiator} is offering to turn {target} into a vampire."
        ]
    },
    "mixer_Vampire_Thirst_RemarkOnLoudHeartbeat": {
        "pre_actions": [
            "{initiator} is noticing {target}'s loud heartbeat and remarking on it, signaling their vampire thirst."
        ]
    },
    "mixer_Vampire_Thirst_ComplimentNeck": {
        "pre_actions": [
            "{initiator} is leaning towards {target} and complimenting their neck, perhaps with a hint of vampire thirst."
        ]
    },
    "mixer_Vampire_Thirst_InquireAboutCardiovascularHealth": {
        "pre_actions": [
            "{initiator}, who is a vampire, is asking {target} about their cardiovascular health."
        ]
    },
    "mixer_social_OfferToCureVampirism_Targeted_Friendly": {
        "pre_actions": [
            "{initiator} is approaching {target} and kindly offering to cure their vampirism."
        ]
    },
    "mixer_social_ThrowVampireCure_Targeted_Mean_AlwaysOn": {
        "pre_actions": [
            "{initiator} is throwing a vampire cure at {target}, with the intention of causing harm or discomfort."
        ]
    },
    "mixer_social_Fight_targeted_mean_SimAndVampire_Duel_WithGarlic": {
        "pre_actions": [
            "{initiator} is confronting {target}, who is a vampire, and is starting a fight with them. Armed with garlic, {initiator} is intending to fend off the vampire and assert their dominance."
        ]
    },
    "mixer_social_Fight_targeted_mean_SimAndVampire_Duel_WithoutGarlic": {
        "pre_actions": [
            "{initiator} is angrily confronting {target} who is revealing themselves as a vampire. A heated battle between them is ensuing, with neither of them holding back."
        ]
    },
    "mixer_social_Fight_targeted_mean_VampireAndSim_Duel_WithGarlic": {
        "pre_actions": [
            "{initiator} is initiating a fight with {target}, where they are engaging in a mean-spirited duel. It seems that {initiator} might be having an advantage since they are a vampire and {target} is armed with garlic."
        ]
    },
    "mixer_social_Fight_targeted_mean_VampireAndSim_Duel_WithoutGarlic": {
        "pre_actions": [
            "{initiator} is engaging in a mean fight with {target}, who is a vampire. The fight is turning into a duel without the use of garlic."
        ]
    },
    "mixer_social_VampiricDuel_Targeted_Mean_VampireToVampire": {
        "pre_actions": [
            "{initiator} is challenging {target} to a vampiric duel, using their powers to engage in a heated confrontation."
        ]
    },
    "mixer_social_Fight_targeted_mean_SimAndVampire_Slay_WithGarlic": {
        "pre_actions": [
            "{initiator} is bravely confronting {target}, who is a mean Sim and a Vampire, armed with garlic to slay them."
        ]
    },
    "mixer_social_Fight_targeted_mean_SimAndVampire_Slay_WithoutGarlic": {
        "pre_actions": [
            "{initiator} is engaging in a fierce battle with {target}, an aggressive vampire. Despite not having any garlic, {initiator} is bravely attempting to slay the vampire."
        ]
    },
    "mixer_social_OfferVampiricTraining_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is extending a friendly offer to {target}, offering to provide them with vampiric training."
        ]
    },
    "mixer_social_RequestVampiricTraining_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} and politely requesting their assistance in receiving vampiric training."
        ]
    },
    "mixer_Vampire_Mentor_MindPower_Generic": {
        "pre_actions": [
            "{initiator} is showing off their mind power skills to {target}, acting as a mentor and demonstrating the impressive abilities of being a vampire."
        ]
    },
    "mixer_Vampire_Mentor_MindPower_Generic_Target": {
        "pre_actions": [
            "{initiator} is using their vampire mind power to teach and guide {target} in practicing mind control techniques."
        ]
    },
    "mixer_Vampire_Mentor_SpiritPower_DrawIn": {
        "pre_actions": [
            "{initiator}, as a vampire mentor, is showing their spirit power to {target} in order to draw them in."
        ]
    },
    "mixer_Vampire_Mentor_SpiritPower_DrawIn_Target": {
        "pre_actions": [
            "{initiator} is acting as a mentor to {target} and is guiding them in practicing their Spirit Power abilities."
        ]
    },
    "mixer_social_VampiricSlay_Targeted_Mean_VampireToVampire_NoDarkForms": {
        "pre_actions": [
            "{initiator} is confronting {target}, a vampire, with the intention to slay them. This interaction is being ruthlessly carried out and is meant specifically for vampires. No dark forms are being involved."
        ]
    },
    "mixer_social_VampiricDuel_Targeted_Mean_VampireToVampire_ActorOnlyDarkForm": {
        "pre_actions": [
            "{initiator} is challenging {target} to a vampiric duel, fueled by their dark vampire forms. This confrontation is being targeted and mean, as the two vampires are battling it out."
        ]
    },
    "mixer_social_VampiricDuel_Targeted_Mean_VampireToVampire_TargetOnlyDarkForm": {
        "pre_actions": [
            "{initiator}, in their dark vampire form, is targeting {target} for a vampiric duel."
        ]
    },
    "mixer_social_VampiricDuel_Targeted_Mean_VampireToVampire_ActorTargetDarkForm": {
        "pre_actions": [
            "{initiator}, in their dark vampire form, is challenging {target}, another vampire, to a fierce and intense duel."
        ]
    },
    "mixer_social_VampiricSlay_Targeted_Mean_VampireToVampire_ActorOnlyDarkForm": {
        "pre_actions": [
            "{initiator}, in their dark form, is viciously attacking {target}, a vampire, with the intent to slay them."
        ]
    },
    "mixer_social_VampiricSlay_Targeted_Mean_VampireToVampire_ActorTargetDarkForm": {
        "pre_actions": [
            "{initiator} is aggressively attacking {target}, intending to slay them as they are a vampire in their dark form."
        ]
    },
    "mixer_social_VampiricSlay_Targeted_Mean_VampireToVampire_TargetOnlyDarkForm": {
        "pre_actions": [
            "{initiator} is aggressively confronting {target} and engaging in a fierce battle to slay them, utilizing their vampiric abilities. This interaction is only possible when both Sims are in their dark vampire forms and can only be performed against other vampires."
        ]
    },
    "mixer_social_Fight_targeted_mean_VampireAndSim_Duel_DarkForm_WithGarlic": {
        "pre_actions": [
            "{initiator} is engaging in a fight with {target}, resulting in a mean and intense confrontation. Avery, being a vampire, is transforming into their dark form and is challenging Charlie to a duel. However, Charlie is coming prepared with garlic to defend themselves."
        ]
    },
    "mixer_social_Fight_targeted_mean_VampireAndSim_Duel_DarkForm_WithoutGarlic": {
        "pre_actions": [
            "{initiator} is confronting {target} in a heated fight, showing no mercy. In a dark and intense duel, {initiator} is revealing their vampire form, overpowering {target} without the use of garlic."
        ]
    },
    "mixer_social_Fight_targeted_mean_SimAndVampire_Duel_DarkForm_WithGarlic": {
        "pre_actions": [
            "{initiator} is confronting {target}, who is a vampire. They are engaging in a heated fight, using mean actions to defend themselves. {initiator} is even transforming into their dark form and bringing out garlic to ward off the vampire."
        ]
    },
    "mixer_social_Fight_targeted_mean_SimAndVampire_Slay_DarkForm_WithGarlic": {
        "pre_actions": [
            "{initiator} is bravely confronting the mean Sim in vampire form, armed with garlic, in a fierce battle to slay the vampire."
        ]
    },
    "mixer_social_Fight_targeted_mean_SimAndVampire_Duel_DarkForm_WithoutGarlic": {
        "pre_actions": [
            "{initiator} is confronting {target}, who is a vampire, in a fierce battle. This heated fight between them is being fueled by {initiator}'s mean-spiritedness and {target}'s dark form. Interestingly, {initiator} isn't even having garlic to use against {target}."
        ]
    },
    "mixer_social_Fight_targeted_mean_SimAndVampire_Slay_DarkForm_WithoutGarlic": {
        "pre_actions": [
            "{initiator} is bravely confronting the mean Sim and vampire {target}, ready to fight and slay them in their dark form, without the need for garlic."
        ]
    },
    "mixer_Vampire_Mentor_SpiritPower_PushOut": {
        "pre_actions": [
            "{initiator}, a Vampire Mentor, is demonstrating their spirit power to {target} by forcefully pushing them out of their way."
        ]
    },
    "mixer_Vampire_Mentor_SpiritPower_PushOut_Target": {
        "pre_actions": [
            "{initiator}, a vampire mentor, is pushing {target} out of their comfort zone as they are practicing their spirit power skills."
        ]
    },
    "mixer_Vampire_Mentor_Instructions_AskQuestions": {
        "pre_actions": [
            "{initiator}, the vampire mentor, is giving instructions to {target} and encouraging them to ask questions."
        ]
    },
    "mixer_Vampire_Mentor_Instructions_PepTalk": {
        "pre_actions": [
            "{initiator} is engaging in an Invisible Mixer with {target}, providing instructions and a pep talk for their vampire mentorship."
        ]
    },
    "mixer_Vampire_Mentor_Instructions_Lecture": {
        "pre_actions": [
            "{initiator} is secretly guiding {target} through a series of instructions and lectures, sharing their wisdom as a vampire mentor."
        ]
    },
    "mixer_social_BatWooHoo_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are transforming into bats and engaging in a romantic WooHoo."
        ]
    },
    "mixer_social_ShowOffPowers_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is using their powers to impress {target}, creating a friendly and targeted interaction."
        ]
    },
    "mixer_social_BatTryForBaby_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are embracing the Bat Try for Baby interaction, as their romance is taking a new and exciting turn."
        ]
    },
    "mixer_Vampire_ShowOffPowers_Actor": {
        "pre_actions": [
            "{initiator} is using their vampire powers to impress and entertain {target}, showing off their abilities like an actor on stage."
        ]
    },
    "mixer_Vampire_ShowOffPowers_Target": {
        "pre_actions": [
            "{initiator}, a vampire, is showing off their powers to {target}."
        ]
    },
    "mixer_social_ShareVampireSecret_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is sharing their knowledge about vampires with {target} in a friendly and targeted conversation."
        ]
    },
    "mixer_Social_VampiricSpar_Targeted_Friendly": {
        "pre_actions": [
            "{initiator} is engaging in a friendly battle of sparring with {target}, using their vampiric powers."
        ]
    },
    "mixer_Social_VampiricSpar_Targeted_Friendly_ActorOnlyDarkForm": {
        "pre_actions": [
            "{initiator} is engaging in a vampiric spar with {target}, using their dark form, in a friendly manner."
        ]
    },
    "mixer_Social_VampiricSpar_Targeted_Friendly_ActorTargetDarkForm": {
        "pre_actions": [
            "{initiator}, in their dark form, is playfully engaging in a friendly spar with {target}, using their vampire powers."
        ]
    },
    "mixer_Social_VampiricSpar_Targeted_Friendly_TargetOnlyDarkForm": {
        "pre_actions": [
            "{initiator} is engaging in a friendly spar with {target} in their dark form, showcasing their vampire skills."
        ]
    },
    "mixer_social_Vampire_MockMortality_Targeted_Mean_AlwaysOn": {
        "pre_actions": [
            "{initiator}, a vampire, is cruelly mocking {target}'s mortality, making mean and targeted remarks."
        ]
    },
    "mixer_social_Vampire_MockPlasmaThirst_Targeted_Mean_AlwaysOn": {
        "pre_actions": [
            "{initiator} is cruelly mocking {target}'s thirst for plasma, deliberately trying to upset them."
        ]
    },
    "mixer_social_Vampire_AskAboutVampireHistory_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in a targeted friendly conversation with {target}, asking them about vampire history."
        ]
    },
    "mixer_social_Vampire_ComplainAboutSunlight_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "As a vampire, {initiator} is complaining to {target} about the harsh effects of sunlight, seeking understanding and sympathy in a friendly way."
        ]
    },
    "mixer_social_Vampire_RecallMortalLife_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is sharing stories from their mortal life with {target}, as they are recalling the memories together."
        ]
    },
    "mixer_social_Vampire_ClaimToBeMasterVampire_Targeted_Mischief_AlwaysOn": {
        "pre_actions": [
            "{initiator} is mischievously claiming to be the Master Vampire to {target}, targeting their knowledge of vampires."
        ]
    },
    "mixer_social_Vampire_LieAboutBadPlasma_Targeted_Mischief_AlwaysOn": {
        "pre_actions": [
            "{initiator}, a vampire, is telling a targeted lie to {target} about bad plasma as a mischievous act."
        ]
    },
    "mixer_social_Vampire_CompareToLongLostLove_Targeted_Romance_MiddleScore": {
        "pre_actions": [
            "{initiator}, a vampire, is comparing {target} to a long-lost love, sparking a romantic interest."
        ]
    },
    "mixer_social_Vampire_MakeVampirePun_Targeted_Funny_AlwaysOn": {
        "pre_actions": [
            "{initiator} is playfully making a vampire pun, targeting {target}, and leading to laughter."
        ]
    },
    "mixer_social_Vampire_PretendToBite_Targeted_Mischief_AlwaysOn": {
        "pre_actions": [
            "{initiator} is pretending to be a vampire and is playfully lunging towards {target} as if to bite them, causing mischief."
        ]
    },
    "mixer_social_TryForBabyInCoffin_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are deciding to take their relationship to the next level by trying for a baby inside a coffin."
        ]
    },
    "mixer_social_WooHooInCoffin_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a romantic WooHoo interaction inside a coffin, transitioning into a more intimate relationship."
        ]
    },
    "mixer_Argument_Start_Politics": {
        "pre_actions": [
            "{initiator} and {target} are starting a heated argument about politics."
        ]
    },
    "mixer_social_Families_Shove": {
        "pre_actions": [
            "{initiator} is forcefully shoving {target}, indicating a tense moment between family members."
        ]
    },
    "mixer_Argument_Start_Careers": {
        "pre_actions": [
            "{initiator} and {target} are getting into a heated argument about their career choices."
        ]
    },
    "mixer_Argument_Start_LifeOutlook": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about their different outlooks on life."
        ]
    },
    "mixer_Argument_Start_Morals": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about their differing morals."
        ]
    },
    "mixer_Argument_Start_Kindness": {
        "pre_actions": [
            "{initiator} is beginning to argue with {target} about the importance of kindness."
        ]
    },
    "mixer_Argument_Start_Humor": {
        "pre_actions": [
            "{initiator} and {target} are getting into an argument about humor."
        ]
    },
    "mixer_Argument_Start_SocialAnxiety": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about social anxiety."
        ]
    },
    "mixer_Argument_Start_NatureWonders": {
        "pre_actions": [
            "{initiator} and {target} are getting into a heated argument about the wonders of nature."
        ]
    },
    "mixer_Argument_Start_Cleanliness": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about cleanliness and the state of their surroundings."
        ]
    },
    "mixer_Argument_Start_Romance": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about their differing opinions on romance."
        ]
    },
    "mixer_Argument_Start_Music": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about music preferences."
        ]
    },
    "mixer_Argument_Start_Sharing": {
        "pre_actions": [
            "{initiator} and {target} are getting into a heated argument about sharing."
        ]
    },
    "mixer_Argument_Start_Arguments": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about arguing and its place in their relationship."
        ]
    },
    "mixer_Argument_Start_School": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about school."
        ]
    },
    "mixer_Argument_Start_Job": {
        "pre_actions": [
            "{initiator} and {target} are getting into a heated argument about their jobs."
        ]
    },
    "mixer_Argument_Start_Parenting": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about parenting methods."
        ]
    },
    "mixer_Argument_Start_HouseRules": {
        "pre_actions": [
            "{initiator} and {target} are getting into a heated argument about the house rules."
        ]
    },
    "mixer_Argument_Start_WhosBetter": {
        "pre_actions": [
            "{initiator} and {target} are starting to argue about who is better."
        ]
    },
    "mixer_Argument_Start_Exercising": {
        "pre_actions": [
            "{initiator} and {target} are getting into a heated argument about exercising and the importance of staying active."
        ]
    },
    "mixer_Argument_Start_LifeGoals": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about their different perspectives on life goals."
        ]
    },
    "mixer_Argument_Start_Children": {
        "pre_actions": [
            "{initiator} and {target} are starting to argue about children."
        ]
    },
    "mixer_Argument_Start_Food": {
        "pre_actions": [
            "{initiator} and {target} are having a heated argument about food preferences and tastes."
        ]
    },
    "mixer_social_Families_Shove_Cont": {
        "pre_actions": [
            "{initiator} is aggressively pushing {target} in a display of hostility."
        ]
    },
    "mixer_social_TalkAboutJournal_targeted_Friendly_HighScore": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} to discuss their journal entries."
        ]
    },
    "mixer_social_MakeFunOfJournal_targeted_mean_highScore": {
        "pre_actions": [
            "{initiator} is mocking {target} for their journal entries, being mean and hurtful."
        ]
    },
    "mixer_social_PoliteIntroduction_greetings_skills": {
        "pre_actions": [
            "{initiator} is approaching {target} with a polite greeting, introducing themselves."
        ]
    },
    "mixer_social_OfferGratitude_Targeted_Friendly_AlwaysOn_invited": {
        "pre_actions": [
            "{initiator} is expressing gratitude towards {target} for their help, in a friendly and inviting manner."
        ]
    },
    "mixer_social_PointOutFlaws_targeted_friendly_alwaysFail": {
        "pre_actions": [
            "{initiator} is kindly pointing out some flaws to {target}, but unfortunately, their attempts are always failing."
        ]
    },
    "mixer_social_CommentOnAppearance_targeted_Friendly_alwaysFail": {
        "pre_actions": [
            "{initiator} is attempting to compliment {target}'s appearance, but it isn't going over well and is always failing."
        ]
    },
    "mixer_social_UnintentionallyCrushDreams_targeted_friendly_alwaysFail": {
        "pre_actions": [
            "{initiator} is unknowingly shattering {target}'s dreams, despite their friendly intentions. Unfortunately, {initiator} is always seeming to fail at this interaction."
        ]
    },
    "mixer_social_AccidentlyInsultInterests_targeted_friendly_alwaysFail": {
        "pre_actions": [
            "{initiator} is unintentionally insulting {target}'s interests, but is quickly trying to rectify the situation with friendly conversation, though their attempt is falling flat and they are continuing to fail to connect."
        ]
    },
    "mixer_social_WhisperAboutCrush_Targeted_Friendly_alwaysOn_Teen": {
        "pre_actions": [
            "{initiator} is discreetly whispering to {target} about their crush, hoping to confide in them and deepen their friendship."
        ]
    },
    "mixer_social_BoastAboutMessingAround_Targeted_Friendly_AlwaysOn_teen": {
        "pre_actions": [
            "{initiator} is proudly boasting to {target} about their adventures in causing mischief, in a friendly and playful manner."
        ]
    },
    "mixer_social_WhineAboutUnfairLife_Targeted_friendly_AlwaysOn_teen": {
        "pre_actions": [
            "{initiator} is complaining to {target} about the unfairness of life."
        ]
    },
    "mixer_social_ObsessAboutFavorite_Targeted_Friendly_AlwaysOn_Teen": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their favorite show, obsessing over every detail."
        ]
    },
    "mixer_social_ShowOffApp_Targeted_Friendly_AlwaysOn_Teen": {
        "pre_actions": [
            "{initiator} is using the Show Off App to show {target} their selfies, in a friendly and targeted manner, particularly appealing to teens."
        ]
    },
    "mixer_social_RaveAboutGrowingUp_targeted_Friendly_AlwaysOn_Teen": {
        "pre_actions": [
            "{initiator} is excitedly raving to {target} about their experiences and memories of growing up as a teen."
        ]
    },
    "mixer_social_PressureToConform_Mean_AlwaysOn_TEen": {
        "pre_actions": [
            "{initiator} is pressuring {target} to conform to societal expectations, using mean-spirited tactics. This interaction is especially common between teenagers."
        ]
    },
    "mixer_social_MockUncoolAdult_Mean_AlwaysOn_Teen": {
        "pre_actions": [
            "{initiator} is mocking {target}, a so-called uncool adult, in a mean-spirited way, displaying their teenage attitude."
        ]
    },
    "mixer_social_ThrowShade_Mean_AlwaysOn_Teen": {
        "pre_actions": [
            "{initiator} is throwing shade at {target}, making mean and sarcastic comments."
        ]
    },
    "mixer_social_ActTough_Mean_AlwaysOn_Teen": {
        "pre_actions": [
            "{initiator} is trying to act tough in front of {target}, perhaps behaving meanly because they are a teenager."
        ]
    },
    "mixer_social_TellUrbanLegend_Mischief_AlwaysOn_Teen": {
        "pre_actions": [
            "{initiator} is sharing a thrilling urban legend with {target}, causing mischief and excitement among the teens."
        ]
    },
    "mixer_social_SpreadRumorsAboutWoohoo_Mischief_AlwaysOn_Teen": {
        "pre_actions": [
            "{initiator} is mischievously spreading rumors about {target} engaging in woohoo, causing potential gossip and controversy among their peers."
        ]
    },
    "mixer_Social_AccuseOfTouchingPossessions_SiblingRivalry_AlwaysOn": {
        "pre_actions": [
            "{initiator} is confronting {target}, accusing them of touching their possessions, fueling their ongoing sibling rivalry."
        ]
    },
    "mixer_Social_BlameForBadMood_SiblingRivalry_AlwaysOn": {
        "pre_actions": [
            "{initiator} is confronting {target} and blaming them for being in a bad mood, possibly due to a sibling rivalry."
        ]
    },
    "mixer_Social_TrickIntoBelieving_SiblingRivalry_AlwaysOn": {
        "pre_actions": [
            "{initiator} is trying to trick {target} into believing in vampires, perhaps as part of a sibling rivalry or playful prank."
        ]
    },
    "mixer_Social_InsultExistence_SiblingRivalry_AlwaysOn": {
        "pre_actions": [
            "{initiator} is spitefully insulting {target}'s very existence, fueling their ongoing sibling rivalry."
        ]
    },
    "mixer_Social_ConvinceMonsterAreReal_SiblingRivalry_AlwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target}, attempting to convince them that monsters are real, possibly fueling a sibling rivalry."
        ]
    },
    "mixer_Social_Tease_SiblingRivalry_AlwaysOn": {
        "pre_actions": [
            "{initiator} is playfully teasing {target} about their face, showcasing a bit of sibling rivalry."
        ]
    },
    "mixer_Social_FlickNose_SiblingRivalry_AlwaysOn": {
        "pre_actions": [
            "{initiator} is playfully flicking {target}'s nose, adding to the sibling rivalry between them."
        ]
    },
    "mixer_social_AskAboutNegativeMood_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} in a friendly manner and asking about their stressed mood, showing genuine concern."
        ]
    },
    "mixer_social_TalkAboutMoodiness_TeenMoodSwing": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} to talk about their moodiness and helping them through a teen mood swing."
        ]
    },
    "mixer_social_CriticizeMoodSwing_TeenMoodSwing": {
        "pre_actions": [
            "{initiator} is criticizing {target} for their mood swing, questioning their behavior as a teenager."
        ]
    },
    "mixer_social_EncourageRedirect_TeenMoodSwing": {
        "pre_actions": [
            "{initiator} is trying to encourage {target} to redirect their mood, especially since {target} is a teenager experiencing mood swings."
        ]
    },
    "mixer_Social_Toddler_Bite": {
        "pre_actions": [
            "{initiator}, a toddler, is playfully biting {target} during a social interaction."
        ]
    },
    "mixer_social_AskAboutFuturePlans_targeted_friendly_alwayson": {
        "pre_actions": [
            "{initiator} is curiously asking {target} about their future plans, in a friendly conversation."
        ]
    },
    "mixer_social_GiveFamilyAdvice_targeted_friendly_alwayson": {
        "pre_actions": [
            "{initiator} is offering some helpful family advice to {target} during their conversation."
        ]
    },
    "mixer_social_BringUpChildhoodMoment_targeted_friendly_alwayson": {
        "pre_actions": [
            "{initiator} is bringing up an embarrassing childhood moment to {target} in a friendly manner."
        ]
    },
    "mixer_social_SecretHandshake_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} and {target} are exchanging a secret handshake, solidifying their friendship."
        ]
    },
    "mixer_social_DeepPersonalConversation_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in a deep and personal conversation with {target}."
        ]
    },
    "mixer_social_BackInMyDay_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is reminiscing about the past with {target}, sharing stories and memories in a friendly conversation."
        ]
    },
    "mixer_social_LovingHug": {
        "pre_actions": [
            "{initiator} is lovingly embracing {target} in a warm hug."
        ]
    },
    "mixer_social_AssertCorrectness_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is confidently asserting their correctness to {target}, in a friendly manner."
        ]
    },
    "mixer_social_MendDifferences_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} in a friendly manner, looking to mend any differences that may exist between them."
        ]
    },
    "mixer_social_TeachAboutResponsibility_Targeted_Friendly_AlwaysOn_Responsible": {
        "pre_actions": [
            "{initiator} is taking the time to teach {target} about responsibility in a friendly and targeted manner."
        ]
    },
    "mixer_social_WhineAboutGrounding_targeted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is complaining to {target} about being grounded, hoping for sympathy or leniency."
        ]
    },
    "mixer_social_SincereApology_targeted_friendly_lowScore": {
        "pre_actions": [
            "{initiator} is approaching {target} and offering a sincere apology, trying to mend their relationship after a low score incident."
        ]
    },
    "mixer_social_FamilyBulletinBoard_WhineAboutCurfew": {
        "pre_actions": [
            "{initiator} is complaining to {target} about their curfew, expressing their frustration."
        ]
    },
    "mixer_UnempatheticSocials_MockMood": {
        "pre_actions": [
            "{initiator} is laughing at {target's} embarrassment, displaying an unempathetic behavior."
        ]
    },
    "mixer_UnempatheticSocials_ScoffMood": {
        "pre_actions": [
            "{initiator} is belittling {target} in a fit of anger, showing no empathy for their feelings. {initiator} is scoffing at {target}."
        ]
    },
    "mixer_social_OtherSims_FixBadRelationship": {
        "pre_actions": [
            "{initiator} is intervening to help fix the strained relationship between {target} and another Sim."
        ]
    },
    "mixer_social_ChildhoodPhases_EncourageEating_targeted_Friendly": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about encouraging better eating habits, especially during childhood phases."
        ]
    },
    "mixer_social_BlameForSchoolProjectDestruction_Targeted_Mean_AlwaysOn": {
        "pre_actions": [
            "{initiator} is confronting {target} and blaming them for the destroyed school project in a mean-spirited manner."
        ]
    },
    "mixer_social_MakeFunnyFaces": {
        "pre_actions": [
            "{initiator} is making funny faces at {target}, trying to make them laugh."
        ]
    },
    "mixer_social_ShareSecret_targeted_Friendly_HighScore_ChildhoodPhase_Clingy": {
        "pre_actions": [
            "{initiator} is sharing a secret with {target}, as part of their friendly interaction. The content of the secret may be related to their childhood phase or it could be something that {initiator} is finding clingy."
        ]
    },
    "mixer_social_TakePictureTogether_targeted_Friendly_alwaysOn_ChildhoodPhase_Clingy": {
        "pre_actions": [
            "{initiator} is asking {target} if they want to take a picture together. They are both striking a friendly pose, capturing a sweet moment of their childhood phase. {initiator} is seeming a bit clingy, wanting to hold onto this memory tightly."
        ]
    },
    "mixer_social_LovingHug_ChildhoodPhase_Clingy": {
        "pre_actions": [
            "{initiator} is giving {target} a loving hug, reminiscent of their childhood phase when they were especially clingy."
        ]
    },
    "mixer_social_Hug_targeted_Friendly_MiddleScore_ChildhoodPhase_Clingy": {
        "pre_actions": [
            "{initiator} is giving {target} a warm hug, showing their friendly and clingy nature, especially during their childhood phase."
        ]
    },
    "mixer_social_BackInMyDay_targeted_friendly_alwaysOn_ParentOnly": {
        "pre_actions": [
            "{initiator} is affectionately reminiscing about the past, sharing stories and experiences with {target} in a friendly manner. This interaction is being exclusively shared between parents."
        ]
    },
    "mixer_social_BlameForSchoolProjectDestruction_Targeted_Mean_AlwaysOn_toddler": {
        "pre_actions": [
            "{initiator} is confronting {target} and blaming them for destroying the school project, using mean and targeted language."
        ]
    },
    "mixer_Argument_Start_Curfew": {
        "pre_actions": [
            "{initiator} and {target} are getting into a heated argument about curfew."
        ]
    },
    "mixer_social_MakeFunnyFaces_Toddler": {
        "pre_actions": [
            "{initiator} is entertaining {target} by making funny faces, amusing the toddler."
        ]
    },
    "mixer_social_DiscussAncientHistory_targeted_Friendly_ArchaeologySkill": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about ancient history, showcasing their knowledge in archaeology skill."
        ]
    },
    "mixer_TellFolkTale_Loop": {
        "pre_actions": [
            "{initiator} is gathering a group around {target} and is beginning to tell a captivating Omiscan folk tale, mesmerizing them with the enchanting story."
        ]
    },
    "mixer_TellFolkTale_Listen": {
        "pre_actions": [
            "{initiator} is telling an Omiscan folk tale to {target}, who is listening intently."
        ]
    },
    "mixer_TellFolkTale_Waiting": {
        "pre_actions": [
            "{initiator} is waiting for an audience to share a captivating folk tale."
        ]
    },
    "mixer_social_CraftSalesTable_Purchase_ArchaeologyTable": {
        "pre_actions": [
            "{initiator} is purchasing an Archaeology Table to craft sales items."
        ]
    },
    "mixer_social_AirKissCheekIntroduction": {
        "pre_actions": [
            "{initiator} is warmly greeting {target} with an air kiss on the cheek, signaling their introduction."
        ]
    },
    "mixer_social_CraftSalesTable_AskAboutNewStock": {
        "pre_actions": [
            "{initiator} is approaching {target} at the Craft Sales Table and asking about the new stock."
        ]
    },
    "mixer_social_CraftSalesTable_Purchase_JungleSupplies": {
        "pre_actions": [
            "{initiator} is visiting the Craft Sales Table to purchase Jungle Supplies."
        ]
    },
    "mixer_Social_Investigation_Act1_QuestionAboutLab": {
        "pre_actions": [
            "{initiator} is approaching {target} and requesting evidence from the secret lab as part of their investigation. They are asking {target} several questions about the lab to gather more information."
        ]
    },
    "mixer_Social_Investigation_Act1_RequestKeycard": {
        "pre_actions": [
            "{initiator} is approaching {target} and politely asking if they can borrow a keycard for an investigation."
        ]
    },
    "mixer_Social_Investigation_Act1_QuestionAboutBase": {
        "pre_actions": [
            "{initiator} is approaching {target} and is requesting evidence from the military base as part of their investigation. They are having a question about the base and are wanting to gather more information."
        ]
    },
    "mixer_Social_Investigation_Act1_ShareConspiracyTheories": {
        "pre_actions": [
            "{initiator} is excitedly sharing conspiracy theories with {target}, hoping to engage them in an investigation into these mysterious theories."
        ]
    },
    "mixer_Social_Investigation_Act1_QuestionAboutMilitaryOperations": {
        "pre_actions": [
            "{initiator} is approaching {target} and requesting evidence regarding the StrangerVille mystery. They are engaging in a social interaction, acting like an investigator, and specifically inquiring about the military operations in Act 1."
        ]
    },
    "mixer_Social_Investigation_AllActs_AskAboutStrangerville": {
        "pre_actions": [
            "{initiator} is engaging in a social conversation with {target} to investigate the mysteries of StrangerVille and is asking about the strange happenings in town."
        ]
    },
    "mixer_Social_Investigation_Act2_TalkAboutSpores": {
        "pre_actions": [
            "{initiator} is approaching {target} in the lab and starting a conversation about spores, wanting to learn more and possibly investigate them together."
        ]
    },
    "mixer_Social_Investigation_Act2_AskToCraftFilter": {
        "pre_actions": [
            "{initiator} is approaching {target} with a request to craft a Spore Filter, as part of an investigation."
        ]
    },
    "mixer_Social_Investigation_Act2_SeduceForScanner": {
        "pre_actions": [
            "{initiator} is attempting to seduce {target} as part of an investigation for the infection scanner."
        ]
    },
    "mixer_Social_Investigation_Act2_PullRank": {
        "pre_actions": [
            "{initiator} is pulling rank on {target} in order to request their assistance with the investigation and use their infection scanner."
        ]
    },
    "mixer_Social_Investigation_Act3_Recruit": {
        "pre_actions": [
            "{initiator} is approaching {target} to recruit them for the fight against the Mother Plant, starting an investigation to see if they're up for the task."
        ]
    },
    "mixer_Social_Possessed_ChatP2P_MakeHumanSound": {
        "pre_actions": [
            "{initiator} is moving their lips to make human sounds while chatting with {target}."
        ]
    },
    "mixer_Social_Possessed_ChatP2N_TalkAboutPlants": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about plants."
        ]
    },
    "mixer_Social_Possessed_ChatP2N_PraisetheMother": {
        "pre_actions": [
            "{initiator} is engaging in a possessed chat with {target} and is praising the Great Mother."
        ]
    },
    "mixer_Social_Possessed_ChatP2N_EnthuseHumanHobbies": {
        "pre_actions": [
            "{initiator} is engaging in a possessed chat with {target}, enthusing about various human hobbies."
        ]
    },
    "mixer_Social_Possessed_ChatP2N_ComplainHumanProblems": {
        "pre_actions": [
            "{initiator} is engaging in a chat with {target} and is beginning to complain about everyday human issues they are facing."
        ]
    },
    "mixer_Social_Possessed_ChatP2N_DiscussHumanThings": {
        "pre_actions": [
            "{initiator} is engaging {target} in a social conversation, discussing various human topics and exchanging thoughts."
        ]
    },
    "mixer_Social_Possessed_ChatP2P_EnthuseMotherPlant": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} to discuss The Great Mother, both being possessed and enthusing about the Mother Plant."
        ]
    },
    "mixer_Social_Possessed_ChatP2P_ConfessFearOfHumans": {
        "pre_actions": [
            "{initiator} is hesitantly approaching {target} and confessing their fear of humans, hoping for understanding and support."
        ]
    },
    "mixer_Social_Possessed_ChatP2P_EmulateHumanLaugh": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a possessed chat, where they both are trying to emulate human laughter."
        ]
    },
    "mixer_Social_Possessed_ChatP2P_Chat": {
        "pre_actions": [
            "{initiator} is initiating a chat with {target} to communicate and have a conversation."
        ]
    },
    "mixer_Social_Investigation_Act1_GiveKeycard": {
        "pre_actions": [
            "{initiator} is discreetly passing a secret lab keycard to {target} as part of their ongoing investigation in Act 1."
        ]
    },
    "mixer_Social_Investigation_Act2_FightForScanner": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument over who gets to use the infection scanner."
        ]
    },
    "mixer_social_AccuseOfSpying": {
        "pre_actions": [
            "{initiator} is confronting {target} and accusing them of spying on them."
        ]
    },
    "mixer_social_ShareConspiracyTheories": {
        "pre_actions": [
            "{initiator} is excitedly sharing a wild conspiracy theory with {target}."
        ]
    },
    "mixer_Social_Investigation_Act2_ImpressWithPhysicalProwess": {
        "pre_actions": [
            "{initiator} is trying to impress {target} by showing off their physical prowess, in order to demonstrate their capabilities for the Infection Scanner investigation."
        ]
    },
    "mixer_Social_MilitaryCareer_Salute": {
        "pre_actions": [
            "{initiator} is saluting {target} as a sign of respect, reflecting their military career."
        ]
    },
    "mixer_Social_MilitaryCareer_Recruit": {
        "pre_actions": [
            "{initiator} is approaching {target} and attempting to recruit them into the military."
        ]
    },
    "mixer_Social_MilitaryCareer_Spar": {
        "pre_actions": [
            "{initiator} is challenging {target} to a friendly spar, testing their combat skills."
        ]
    },
    "mixer_Social_MilitaryCareer_OrderTo_DropAndGive20": {
        "pre_actions": [
            "{initiator} is giving a military order to {target} to drop and give them 20 push-ups."
        ]
    },
    "mixer_Social_MilitaryCareer_OrderTo_RunALap": {
        "pre_actions": [
            "{initiator} is giving {target} the order to run a lap as part of their military career training."
        ]
    },
    "mixer_Social_MilitaryCareer_OrderTo_Attention": {
        "pre_actions": [
            "{initiator} is calling out to {target}, commanding them to pay attention immediately."
        ]
    },
    "mixer_Social_MilitaryCareer_OrderTo_CleanThisPlaceUp": {
        "pre_actions": [
            "{initiator} is instructing {target}, who is in the military career, to clean up the place."
        ]
    },
    "mixer_Social_MilitaryCareer_OrderTo_Spar": {
        "pre_actions": [
            "{initiator} is challenging {target} to a friendly spar, in order to test their combat skills."
        ]
    },
    "mixer_Social_MilitaryCareer_ShareWarStories": {
        "pre_actions": [
            "{initiator} and {target}, both with military careers, are engaging in a conversation and sharing war stories."
        ]
    },
    "mixer_Social_MilitaryCareer_Spar_NoTests": {
        "pre_actions": [
            "{initiator} is engaging in a spar with {target} as part of their military career, without any tests involved."
        ]
    },
    "mixer_social_BragAboutBeatingMotherPlant": {
        "pre_actions": [
            "{initiator} is excitedly telling a story to {target} about their epic victory over the Mother Plant."
        ]
    },
    "mixer_Social_MilitaryCareer_Interrogate": {
        "pre_actions": [
            "{initiator} is questioning {target} with a serious tone, as part of their military career training."
        ]
    },
    "mixer_Social_MilitaryCareer_GiveInspirationalSpeech": {
        "pre_actions": [
            "{initiator} is giving an inspirational speech to motivate {target} in their military career."
        ]
    },
    "mixer_Social_Investigation_Act1_QuestionAboutBaseOrLab": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking them about the military base, hoping to gather more information for an investigation."
        ]
    },
    "mixer_Social_Investigation_Act3_Recruit_DisplayOnly": {
        "pre_actions": [
            "{initiator} is approaching {target} and engaging in a social conversation, investigating their skills and abilities to potentially recruit them for the fight against the Mother Plant. However, this interaction is purely display-only and is not leading to actual recruitment."
        ]
    },
    "mixer_Social_Investigation_Act2_BribeForScanner": {
        "pre_actions": [
            "{initiator} is attempting to bribe {target} in order to obtain a scanner for their investigation in Act 2."
        ]
    },
    "mixer_social_MilitaryIntroduction_greetings": {
        "pre_actions": [
            "{initiator}, in their military uniform, is approaching {target} and is offering a formal military introduction and greeting."
        ]
    },
    "mixer_social_Fight_targeted_mean_PunchableFace": {
        "pre_actions": [
            "{initiator} is confronting {target}, ready to fight and exchange punches due to a mean comment or appearance that provoked them."
        ]
    },
    "mixer_social_Fight_targeted_SummonGhost_Fail": {
        "pre_actions": [
            "{initiator} is trying to start a fight with {target}, but is failing to summon a ghost."
        ]
    },
    "mixer_Socials_WitchPerks_Socialite_EnthuseAboutMagic": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about magic, sharing their enthusiasm for all things witchy."
        ]
    },
    "mixer_Socials_WitchPerks_Socialite_DiscussOverchargeRisks": {
        "pre_actions": [
            "{initiator}, a Witch, is engaging in a conversation with {target} to discuss the risks of overcharging spells."
        ]
    },
    "mixer_Socials_WitchPerks_Socialite_TalkAboutPotionMishaps": {
        "pre_actions": [
            "{initiator}, a witch with Socialite perks, is engaging in a conversation with {target} to discuss their various mishaps with potions."
        ]
    },
    "mixer_Social_WitchOccult_MagicTraining_Offer": {
        "pre_actions": [
            "{initiator} is offering {target} magical training, recognizing their interest in the occult and knowledge of magic."
        ]
    },
    "mixer_Social_WitchOccult_MagicTraining_Request": {
        "pre_actions": [
            "{initiator} is approaching {target}, an experienced witch, and is asking if they can receive magical training."
        ]
    },
    "mixer_Social_WitchOccult_RiteOfDissolution_Request": {
        "pre_actions": [
            "{initiator} is approaching {target}, a fellow witch, and asking for the Rite of Dissolution, a special occult request."
        ]
    },
    "mixer_Social_WitchOccult_RiteOfAscension_Request": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking about the Rite of Ascension, seeking guidance as a fellow witch."
        ]
    },
    "mixer_Social_WitchOccult_RiteOfAscension_Offer": {
        "pre_actions": [
            "{initiator} is offering {target} the Rite of Ascension, a special ritual known only to witches in the occult community."
        ]
    },
    "mixer_Sabacc_Cheat": {
        "pre_actions": [
            "{initiator} is attempting to cheat at a game of Sabacc with {target}."
        ]
    },
    "mixer_social_Batuu_Reputation_EnthuseAbout_CrushingResistance": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their reputation on Batuu and is enthusing about crushing the resistance."
        ]
    },
    "mixer_social_Batuu_Reputation_EnthuseAbout_StoppingFirstOrder": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their reputation and their shared goal of stopping the First Order."
        ]
    },
    "mixer_social_Batuu_Reputation_EnthuseAbout_GalacticSkimmers": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about Galactic Credit Skimmers, showcasing their knowledge of Batuu and trying to impress them with their enthusiasm for the topic."
        ]
    },
    "mixer_social_Batuu_Reputation_TellTalesofGalacticConquest": {
        "pre_actions": [
            "{initiator} is excitedly sharing stories of their exploits in galactic conquest with {target}, hoping to build their reputation and impress them."
        ]
    },
    "mixer_social_Batuu_Reputation_TellTalesofSmuggling": {
        "pre_actions": [
            "{initiator} is sharing exciting stories of smuggling with {target}, using their Batuu reputation to capture their interest."
        ]
    },
    "mixer_social_Batuu_Reputation_TellTalesOfGalacticAdventure": {
        "pre_actions": [
            "{initiator} is excitedly recounting thrilling tales of their adventures on Batuu to {target}, hoping to impress them and enhance their own reputation."
        ]
    },
    "mixer_social_Batuu_Reputation_HatchElaboratePlan": {
        "pre_actions": [
            "{initiator} and {target} are hatching an elaborate plan together to improve their reputation on Batuu."
        ]
    },
    "mixer_social_Batuu_Reputation_Recruit_FirstOrder": {
        "pre_actions": [
            "{initiator} is trying to convince {target} to enlist in the First Order, leveraging their reputation on Batuu as a recruit."
        ]
    },
    "mixer_social_Batuu_Reputation_Recruit_Resistance": {
        "pre_actions": [
            "{initiator} is passionately speaking to {target}, urging them to join the Resistance in Batuu."
        ]
    },
    "mixer_Social_Batuu_Hondo_DiscussShippingCompany": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} about a legitimate shipping company, possibly involving Hondo, on Batuu."
        ]
    },
    "mixer_Social_Batuu_Hondo_AskAboutMissingCredits": {
        "pre_actions": [
            "{initiator} is approaching {target} on Batuu and asking about the missing credits."
        ]
    },
    "mixer_Social_Batuu_Vi_Distraction": {
        "pre_actions": [
            "{initiator} is attempting to distract {target} while visiting Batuu to divert their attention from something."
        ]
    },
    "mixer_Social_Batuu_Vi_ShareRumors": {
        "pre_actions": [
            "{initiator} is sharing some interesting rumors that they overheard on Batuu with {target}."
        ]
    },
    "mixer_Social_Batuu_Vi_DiscussStrategy": {
        "pre_actions": [
            "{initiator} and {target}, both from Batuu Vi, are discussing their recruitment strategy."
        ]
    },
    "mixer_Social_Batuu_Vi_DiscussFO": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a social conversation, discussing the movements of the First Order on Batuu."
        ]
    },
    "mixer_Social_Batuu_Agnon_DiscussIndividuals": {
        "pre_actions": [
            "{initiator} is engaging in a social conversation with {target} about suspicious individuals they are encountering on Batuu, specifically discussing Agnon."
        ]
    },
    "mixer_Social_Batuu_Agnon_QuestionLoyalty": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} on Batuu, asking about their loyalty."
        ]
    },
    "mixer_Social_Batuu_Agnon_DebateLocation": {
        "pre_actions": [
            "{initiator} is engaging in a social debate with {target} on the Batuu planet, discussing the location of the Resistance base."
        ]
    },
    "mixer_social_Fight_targeted_Intimidate_For_Info": {
        "pre_actions": [
            "{initiator} is confronting {target} in a heated argument, attempting to intimidate them into revealing information."
        ]
    },
    "mixer_Social_Batuu_SNPC_Kylo_QuestionLoyalty": {
        "pre_actions": [
            "{initiator} is approaching Kylo, a Batuu SNPC, and questioning his loyalty."
        ]
    },
    "mixer_social_Fight_targeted_CheckID_CriminalFight": {
        "pre_actions": [
            "{initiator} is confronting {target} in a heated argument, resulting in a physical fight."
        ]
    },
    "mixer_social_Fight_targeted_mean_SabaccCheater": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated fight after suspecting {target} of cheating during a game of Sabacc."
        ]
    },
    "mixer_social_Fight_Batuu_Inspection_ActorIsFO": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a fight, using batuus as weapons. It appears that the fight is part of an inspection and the initiator might be an actor portraying a character."
        ]
    },
    "mixer_social_Batuu_Mission_RS7_Fight_For_FirstOrder_Uniform": {
        "pre_actions": [
            "{initiator} and {target} are engaging in an intense fight for the First Order uniform during the Batuu Mission RS7."
        ]
    },
    "mixer_Social_Batuu_Mission_ShareTalesOfMisdeeds_SS10": {
        "pre_actions": [
            "{initiator} is sharing tales of their misdeeds with {target}, recounting their adventures during a Batuu mission."
        ]
    },
    "mixer_social_Batuu_Mission_SS17_Fight_For_Valuable_Information": {
        "pre_actions": [
            "{initiator} is confronting {target} in a heated argument, desperately trying to extract valuable information for their Batuu mission."
        ]
    },
    "mixer_social_Fight_targeted_Rich_Scoundrel_Valuable": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated fight over a valuable item, as both Sims are rich scoundrels."
        ]
    },
    "mixer_social_Fight_targeted_mean_RecruitToFO_ResistanceTarget_FR3": {
        "pre_actions": [
            "{initiator} is initiating a fight with {target}, using mean tactics in an attempt to recruit them to the Freelancer Resistance Faction."
        ]
    },
    "mixer_social_WooHooDwelling_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking off to a private place in the dwelling to engage in a romantic encounter, taking their relationship to the next level."
        ]
    },
    "mixer_social_Fight_targeted_mean_FS6_IntimidateFight": {
        "pre_actions": [
            "{initiator} is aggressively confronting {target} in a heated exchange, attempting to intimidate them into submission."
        ]
    },
    "mixer_social_Fight_targeted_mean_FS4_ThreatenArrest": {
        "pre_actions": [
            "{initiator} and {target} are getting into a heated argument and are ending up in a physical fight. {initiator} is threatening {target} with arrest."
        ]
    },
    "mixer_Social_Batuu_EnthuseAbout_Droids": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their love for droids on Batuu."
        ]
    },
    "mixer_Social_Batuu_EnthuseAbout_Wookiees": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} about Wookiees, expressing enthusiasm and interest in the topic."
        ]
    },
    "mixer_Social_Batuu_EnthuseAbout_Lightsabers": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about Lightsabers, expressing their love and enthusiasm for them, particularly during their visit to Batuu."
        ]
    },
    "mixer_Social_Batuu_EnthuseAbout_Batuu": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their recent trip to Batuu, enthusing about their experiences on the planet."
        ]
    },
    "mixer_Social_Batuu_EnthuseAbout_Sabacc": {
        "pre_actions": [
            "{initiator} and {target} are chatting about Sabacc, enthusiastically discussing their favorite strategies and experiences on Batuu."
        ]
    },
    "mixer_Social_Batuu_EnthuseAbout_TheForce": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} about The Force, expressing enthusiasm and sharing knowledge about it."
        ]
    },
    "mixer_Social_Batuu_EnthuseAbout_Datapads": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a social conversation about Datapads, expressing enthusiasm and sharing knowledge about this topic on Batuu."
        ]
    },
    "mixer_Social_Batuu_EnthuseAbout_Starships": {
        "pre_actions": [
            "{initiator} and {target} are chatting animatedly about Starfighters on Batuu, passionately discussing their favorite starships and their features."
        ]
    },
    "mixer_social_BrightenDay_targeted_friendly_emotionSpecific_Batuu_SNPC": {
        "pre_actions": [
            "{initiator} is performing a friendly gesture to {target} in an effort to brighten their day, like those interactions with Batuu Star Wars non-playable characters (SNPCs)."
        ]
    },
    "mixer_social_DeclareEnemy_targeted_mean_relationship_Batuu_SNPC": {
        "pre_actions": [
            "{initiator} is declaring {target} as their enemy, solidifying their mean relationship. This interaction is taking place in Batuu with an SNPC."
        ]
    },
    "mixer_social_SuggestBoldHomeMakeoverIdeas_targeted_Friendly_alwaysOn_career_InteriorDecorator": {
        "pre_actions": [
            "{initiator}, who is an Interior Decorator, is friendly suggesting some bold home makeover ideas to {target}."
        ]
    },
    "mixer_social_DiscussLatestTrends_targeted_Friendly_alwaysOn_career_InteriorDecorator": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about the latest trends, particularly in the field of interior decorating."
        ]
    },
    "mixer_social_DiscussLatestTrends_targeted_Friendly_alwaysOn_career_InteriorDecorator_Interview": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} to discuss the latest trends in the interior decorating industry, as part of an interview."
        ]
    },
    "mixer_social_SuggestBoldHomeMakeoverIdeas_targeted_Friendly_alwaysOn_career_InteriorDecorator_Interview": {
        "pre_actions": [
            "{initiator} is excitedly suggesting bold home makeover ideas to {target}, sharing their expertise as an interior decorator during a friendly conversation, possibly for an interview."
        ]
    },
    "mixer_social_UnflirtyTrait_GiveColdShoulder_Targeted_Mean_AlwaysOn": {
        "pre_actions": [
            "{initiator}, who has the Unflirty trait, is intentionally ignoring {target} and giving them the cold shoulder as a mean gesture."
        ]
    },
    "mixer_social_UnflirtyTrait_ReprimandPublicIntimacy_Targeted_Mean_AlwaysOn": {
        "pre_actions": [
            "{initiator}, with their unflirty trait, is reprimanding {target} for engaging in public intimacy."
        ]
    },
    "mixer_social_MakeSmallTalk_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in friendly conversation with {target}, making small talk to break the ice."
        ]
    },
    "mixer_PerformanceSpace_solicitTip": {
        "pre_actions": [
            "{initiator} is approaching {target} in the performance space, solicitating tips for their performance."
        ]
    },
    "mixer_social_AskAboutCulturalFoods_targeted_Friendly": {
        "pre_actions": [
            "{initiator} is asking {target} about local cuisine and is showing a friendly interest in learning more about different cultural foods."
        ]
    },
    "mixer_social_RecommendLocalBar_friendly_NT": {
        "pre_actions": [
            "{initiator} is suggesting to {target} that they should check out a local bar together, in a friendly and non-threatening manner."
        ]
    },
    "mixer_social_ComplainAboutLoudNoises_targeted_Mean_alwaysOn_apartmentNeighbor": {
        "pre_actions": [
            "{initiator} is approaching {target} and angrily complaining about the loud noises coming from their apartment neighbor."
        ]
    },
    "mixer_social_RecommendLocalMuseum_friendly_NT": {
        "pre_actions": [
            "{initiator} is recommending a local museum to {target}, while engaging in a friendly conversation."
        ]
    },
    "mixer_social_RecommendLocalClub_friendly_NT": {
        "pre_actions": [
            "{initiator} is suggesting to {target} that they should check out a local nightclub. They are coming across as friendly and easygoing."
        ]
    },
    "mixer_social_RaveAboutFamousSingers_targeted_Friendly_alwaysOn_skills": {
        "pre_actions": [
            "{initiator} is excitedly raving to {target} about their favorite singers."
        ]
    },
    "mixer_social_RecommendLocalRestaurant_friendly_NT": {
        "pre_actions": [
            "{initiator} is enthusiastically recommending a local restaurant to {target} during a friendly conversation."
        ]
    },
    "mixer_social_Fight_targeted_ApartmentNeighborSituation_LoudNoises": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument, causing loud noises in their apartment neighbor situation."
        ]
    },
    "mixer_Shower_SingInShower": {
        "pre_actions": [
            "{initiator} is happily singing in the shower."
        ]
    },
    "mixer_Social_Friendly_VideoGameConsole_Win2Win": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about winning a game on the video game console, engaging in a friendly conversation."
        ]
    },
    "mixer_Social_Friendly_VideoGameConsole_Win2Lose": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} about their recent win in a video game, eager to share their victory."
        ]
    },
    "mixer_Social_Friendly_VideoGameConsole_Lose2Lose": {
        "pre_actions": [
            "{initiator} and {target} are sitting down together on the couch, commiserating about their recent losses in the video game console tournament."
        ]
    },
    "mixer_Social_Friendly_VideoGameConsole_Lose2Win": {
        "pre_actions": [
            "{initiator} is approaching {target} and congratulating them on winning a game together on the video game console. {initiator} is admiring {target}'s skill and sportsmanship."
        ]
    },
    "mixer_social_Propose_targeted_romance_relationship_BlossomFestival": {
        "pre_actions": [
            "{initiator} is getting caught up in the heat of the moment during the Blossom Festival and is deciding to propose a romantic relationship to {target}."
        ]
    },
    "mixer_social_MentionFlirtyVibe_Festival_Blossom_targeted_romance": {
        "pre_actions": [
            "{initiator} is mentioning the flirty festival vibe to {target}, hinting at a potential romantic connection that is blooming between them."
        ]
    },
    "mixer_social_JokeGettingTogether_Festival_Blossom_targeted_romance": {
        "pre_actions": [
            "{initiator} is playfully joking with {target} about them getting together, possibly during the Festival of Blossoms, adding a touch of romance to the conversation."
        ]
    },
    "mixer_social_FlirtyDream_Festival_Blossom_targeted_romance": {
        "pre_actions": [
            "{initiator} is sharing a flirty dream about {1.SimFirstName}, inspired by the festival and the essence of blossoming romance."
        ]
    },
    "mixer_social_HeatofMomentPassion_Festival_Blossom_targeted_romance": {
        "pre_actions": [
            "{initiator} is confessing their feelings to {target} in the heat of the moment at the Festival of Blossom, igniting a passionate romance between them."
        ]
    },
    "mixer_bubbleBottle_BlowBubbles": {
        "pre_actions": [
            "{initiator} is taking out a bubble bottle and starting to blow bubbles in front of {target}, hoping to create a playful and lighthearted atmosphere."
        ]
    },
    "mixer_social_BragCurryContest_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} and excitedly bragging about being the reigning Curry Champion."
        ]
    },
    "mixer_social_AskAboutRomanticDestiny_targeted_Friendly_AlwaysOn_LoveGuru": {
        "pre_actions": [
            "{initiator} is approaching {target} with a friendly demeanor and is asking about their romantic destiny, seeking guidance as a Love Guru."
        ]
    },
    "mixer_social_RequestGuruLoveWisdom_targeted_Friendly_AlwaysOn_LoveGuru": {
        "pre_actions": [
            "{initiator} is approaching {target}, the Romance Guru, to request their wisdom and advice on matters of love. The interaction is friendly and is seeking guidance in the realm of romance."
        ]
    },
    "mixer_social_AskGuruAboutCurrentRelationship_targeted_Friendly_AlwaysOn_LoveGuru": {
        "pre_actions": [
            "{initiator} is approaching Love Guru {target} and asking them for advice on their current relationship."
        ]
    },
    "mixer_social_AskAboutRomanticDestiny_Targeted_Friendly_AlwaysOn_LoveGuru_Initiate": {
        "pre_actions": [
            "{initiator} is approaching {target} with a friendly demeanor and is asking about their romantic destiny, seeking advice from the Love Guru."
        ]
    },
    "mixer_social_RequestGuruLoveWisdom_Targeted_Friendly_AlwaysOn_STC_LoveGuru_Initiate": {
        "pre_actions": [
            "{initiator} is approaching {target} with a friendly and targeted request, seeking their wisdom as a Love Guru."
        ]
    },
    "mixer_social_AskGuruAboutCurrentRelationship_Targeted_Friendly_AlwaysOn_STC_LoveGuru_Initiate": {
        "pre_actions": [
            "{initiator} is approaching the Love Guru and asking for advice about their current relationship with {target} in a friendly and targeted manner."
        ]
    },
    "mixer_Social_RantAboutShow_Targeted_Friendly_AlwaysOn_STC_LogicFestival": {
        "pre_actions": [
            "{initiator} is approaching {target} and sharing their frustration about a TV show being cancelled, engaging in a friendly rant about it."
        ]
    },
    "mixer_Social_TalkAboutCosplayers_Targeted_Friendly_AlwaysOn_STC_LogicFestival": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, discussing their admiration for cosplayers at the logic festival."
        ]
    },
    "mixer_Social_ArgueGif_Targeted_Friendly_AlwaysOn_STC_LogicFestival": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument about the pronunciation of 'Gif' during the Logic Festival event."
        ]
    },
    "mixer_Social_DebateAntBears_Targeted_Friendly_AlwaysOn_STC_LogicFestival": {
        "pre_actions": [
            "{initiator} is engaging in a friendly debate with {target} about the hypothetical scenario of 1000 ant-sized bears versus 1 bear-sized ant, using logical arguments. This is taking place at a logic festival."
        ]
    },
    "mixer_Socials_JokeAboutPi_Targeted_Funny_AlwaysOn_STC_LogicFestival": {
        "pre_actions": [
            "{initiator} is telling a hilarious joke about Pi to {target} during the Logic Festival."
        ]
    },
    "mixer_Socials_JokeAboutRocketWoohoo_Targeted_Funny_AlwaysOn_STC_LogicFestival": {
        "pre_actions": [
            "{initiator} is playfully telling a hilarious joke to {target} about rocket ship woohoo, making everyone laugh at the Logic Festival."
        ]
    },
    "mixer_social_Career_Activist_MakeEmptyPromises_alwaysOn": {
        "pre_actions": [
            "{initiator} is trying to impress {target} by making empty promises about their career achievements as an activist."
        ]
    },
    "mixer_Social_SelfieWithCosplayer_Targeted_Friendly_AlwaysOn_STC_LogicFestival": {
        "pre_actions": [
            "{initiator} is approaching the cosplayer at the Logic Festival and asking to take a selfie with them. They are striking up a friendly conversation while capturing the moment."
        ]
    },
    "mixer_social_GossipSakuraTea_Festival_Blossom_targeted_friendly": {
        "pre_actions": [
            "{initiator} is excitedly sharing some gossip with {target} about the effects of Sakura Tea at the festival. They are engaging in a friendly conversation about the blossoms and the positive effects of the tea."
        ]
    },
    "mixer_social_Festival_Blossom_TransitionToIntimate_Sleaze_KissCheek": {
        "pre_actions": [
            "{initiator} is leaning in and planting a gentle kiss on {target}'s cheek during the festival, a sweet gesture that is signaling a transition to a more intimate level of the relationship."
        ]
    },
    "mixer_social_Festival_Blossom_TransitionToIntimate_Sleaze_DipKiss": {
        "pre_actions": [
            "{initiator} and {target} are sharing an intimate moment at the festival by exchanging a sweet and romantic kiss, allowing their relationship to transition to a more intimate level."
        ]
    },
    "mixer_social_Festival_Blossom_TransitionToIntimate_Sleaze_Whisper": {
        "pre_actions": [
            "{initiator} is leaning close to {target} during the festival, whispering sweet nothings in their ear."
        ]
    },
    "mixer_social_Festival_Blossom_TransitionToIntimate_Sleaze_ShowGuns": {
        "pre_actions": [
            "{initiator} is attending the Festival of Blossom and flirting with {target} in a somewhat sleazy manner, showcasing their impressive gun handling skills."
        ]
    },
    "mixer_DogLoverTrait_EnthuseAboutDogs": {
        "pre_actions": [
            "{initiator}, who has the Dog Lover trait, is excitedly talking to {target} about dogs and sharing their love for them."
        ]
    },
    "mixer_CatLoverTrait_EnthuseAboutCats": {
        "pre_actions": [
            "{initiator}, who has the Cat Lover trait, is enthusiastically talking to {target} about cats."
        ]
    },
    "mixer_DogLoverTrait_ShareLoveOfDogs": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} about their love for dogs, bonding over their shared passion."
        ]
    },
    "mixer_CatLoverTrait_ShareLoveOfCats": {
        "pre_actions": [
            "{initiator}, possessing the Cat Lover trait, is sharing their love of cats with {target}, discussing their favorite breeds and funny cat videos."
        ]
    },
    "mixer_Social_Targeted_PetToPet_Greeting_Hostile": {
        "pre_actions": [
            "{initiator} is approaching {target} in a hostile manner during a pet-to-pet greeting."
        ]
    },
    "mixer_Dog_Training_Human_Heel": {
        "pre_actions": [
            "The human is instructing the dog to walk beside them, using the command \"heel.\""
        ]
    },
    "mixer_Dog_Training_Human_Sit": {
        "pre_actions": [
            "{initiator} is commanding {target} to sit during a dog training session."
        ]
    },
    "mixer_Dog_Training_Human_Speak": {
        "pre_actions": [
            "{initiator} is training the dog to respond to verbal commands by teaching it to speak on command."
        ]
    },
    "mixer_Dog_Training_Human_LieDown": {
        "pre_actions": [
            "{initiator} is commanding {target} to lie down as part of dog training."
        ]
    },
    "mixer_Dog_Training_Human_RollOver": {
        "pre_actions": [
            "The human is commanding the dog to roll over and the dog is obediently performing the trick."
        ]
    },
    "mixer_Dog_Training_Human_Fetch": {
        "pre_actions": [
            "{initiator} is throwing a ball and instructing {target} to fetch it as part of their dog training."
        ]
    },
    "mixer_Dog_Training_Human_PlayDead": {
        "pre_actions": [
            "The human is instructing the dog to play dead during a training session."
        ]
    },
    "mixer_Dog_Training_Human_Shake": {
        "pre_actions": [
            "{initiator} is teaching {target} how to do a shake."
        ]
    },
    "mixer_Social_Targeted_PetToPet_Greeting_Friendly": {
        "pre_actions": [
            "{initiator} is approaching {target} in a friendly manner, greeting them and engaging in a pet-to-pet interaction."
        ]
    },
    "mixer_Social_Targeted_PetToPet_Greeting_Neutral": {
        "pre_actions": [
            "{initiator} is approaching {target} to greet them in a neutral manner, possibly with a pet-to-pet interaction."
        ]
    },
    "mixer_Dog_Training_Human_Shake_Command": {
        "pre_actions": [
            "{initiator} is training {target} to shake hands using the command 'shake'."
        ]
    },
    "mixer_Dog_Training_Human_Practice": {
        "pre_actions": [
            "{initiator} is engaging in dog training with {target}, practicing tricks and commands."
        ]
    },
    "mixer_social_IntroDog_greetings": {
        "pre_actions": [
            "{initiator} is introducing {2.SimFirstName} to {target} by allowing them to exchange friendly greetings."
        ]
    },
    "mixer_social_WooHooLighthouse_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking off to the lighthouse for a romantic encounter and a transition into a new level of intimacy."
        ]
    },
    "mixer_social_TryForBabyLighthouse_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking off to the lighthouse for a romantic moment, hoping to try for a baby."
        ]
    },
    "mixer_Dog_Training_Human_Shake_Demo": {
        "pre_actions": [
            "{initiator} is teaching {target} how to shake hands as a demonstration of dog training."
        ]
    },
    "mixer_Social_Friendly_DeclareTemperaturePreference_Cool": {
        "pre_actions": [
            "{initiator} is expressing their preference for cool temperatures to {target}, in a friendly conversation."
        ]
    },
    "mixer_Social_Friendly_DeclareTemperaturePreference_Warm": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, expressing their preference for warmer temperatures."
        ]
    },
    "mixer_Social_Friendly_DeclareTemperaturePreference_None": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, without discussing any specific temperature preference."
        ]
    },
    "mixer_Social_Friendly_DeclareWeatherHate_Sun": {
        "pre_actions": [
            "{initiator} is expressing their annoyance to {target} about the intense heat of the sun."
        ]
    },
    "mixer_Social_Friendly_DeclareWeatherHate_Wind": {
        "pre_actions": [
            "{initiator} is expressing their dislike for the wind to {target} in a friendly manner."
        ]
    },
    "mixer_Social_Friendly_DeclareWeatherHate_Rain": {
        "pre_actions": [
            "{initiator} and {target} are bonding over their dislike for rainy weather."
        ]
    },
    "mixer_Social_Friendly_DeclareWeatherHate_Snow": {
        "pre_actions": [
            "{initiator} is playfully throwing a snowball at {target}, expressing their dislike for the snow."
        ]
    },
    "mixer_Social_Friendly_DeclareWeatherHate_None": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a friendly conversation, expressing their dislike for any particular weather."
        ]
    },
    "mixer_Social_Friendly_DeclareWeatherLove_None": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly conversation about their love for weather, without any particular weather in mind."
        ]
    },
    "mixer_Social_Friendly_DeclareWeatherLove_Rain": {
        "pre_actions": [
            "{initiator} and {target} are enjoying the rain together, declaring their love for the weather."
        ]
    },
    "mixer_Social_Friendly_DeclareWeatherLove_Snow": {
        "pre_actions": [
            "{initiator} is excitedly approaching {target} and declaring their love for the snow, sparking a friendly conversation."
        ]
    },
    "mixer_Social_Friendly_DeclareWeatherLove_Sun": {
        "pre_actions": [
            "{initiator} and {target} are enjoying a friendly conversation under the warm sun, expressing their love for the beautiful weather."
        ]
    },
    "mixer_Social_Friendly_DeclareWeatherLove_Wind": {
        "pre_actions": [
            "{initiator} is embracing the windy weather and joyfully declaring their love for it to {target}, engaging in a friendly conversation."
        ]
    },
    "mixer_social_Targeted_Friendly_TalkAboutClimateChange": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} to talk about climate change."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_TalkAboutWeather": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} about the current weather."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_TalkAboutTemperature": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target}, discussing the current temperature."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutRain": {
        "pre_actions": [
            "{initiator} is approaching {target} and complaining about the rain, expressing their dissatisfaction with the current weather conditions."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutSnow": {
        "pre_actions": [
            "{initiator} is expressing their frustration about the snow to {target}."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutCloudyWeather": {
        "pre_actions": [
            "{initiator} is complaining to {target} about the cloudy weather."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutSunnyWeather": {
        "pre_actions": [
            "{initiator} is complaining to {target} about the sunny weather."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutWindyWeather": {
        "pre_actions": [
            "{initiator} is grumbling to {target} about the windy weather."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutThunderstorms": {
        "pre_actions": [
            "{initiator} is complaining to {target} about the thunderstorms and is expressing their dislike for them."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutFreezingTemperature": {
        "pre_actions": [
            "{initiator} is complaining to {target} about the freezing temperature and how cold it is."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutHotTemperature": {
        "pre_actions": [
            "{initiator} is expressing their frustration about the heat to {target}, complaining about the hot temperature."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_ComplainAboutBurningTemperature": {
        "pre_actions": [
            "{initiator} is complaining to {target} about the heatwave and how hot it is."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_HugOutCold": {
        "pre_actions": [
            "{initiator} is seeing that {target} is feeling cold due to the weather and is offering a warm hug to help them feel better."
        ]
    },
    "mixer_social_WeatherTemperatureSocials_WarmUp": {
        "pre_actions": [
            "{initiator} is suggesting {target} to warm up together with their body heat, given the weather and temperature."
        ]
    },
    "mixer_social_Fight_targeted_SurpriseHoliday_BattleRoyale": {
        "pre_actions": [
            "{initiator} and {target} are unexpectedly engaging in a fierce battle, turning a holiday gathering into a surprise-filled battle royale."
        ]
    },
    "mixer_social_DiscussTVPremiere_Targeted_Friendly": {
        "pre_actions": [
            "{initiator} is engaging in a targeted and friendly conversation with {target} to discuss the details of the season premiere of their favorite TV show."
        ]
    },
    "mixer_Social_TVPremiere_SpoilEpisode": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about the latest season premiere of a TV show, unknowingly spoiling the episode."
        ]
    },
    "mixer_social_Fight_targeted_SurpriseHoliday_BattleRoyale_Transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a surprise holiday battle royale, resulting in a fierce fight."
        ]
    },
    "mixer_social_WooHooInLeafPile_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a romantic WooHoo session in a leaf pile, transitioning from casual conversation to more intimate activities."
        ]
    },
    "mixer_social_TryForBabyInLeafPile_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are deciding to try for a baby together, while having a romantic interaction in a leaf pile."
        ]
    },
    "mixer_social_Mistletoe_kiss": {
        "pre_actions": [
            "{initiator} is trying to steal a kiss from {target} under the mistletoe."
        ]
    },
    "mixer_Social_ShareResolution_targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is sharing a resolution with {target}, fostering a friendly and social interaction."
        ]
    },
    "mixer_social_EnthuseAboutGardenerCareer_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly sharing their love for gardening with {target}, discussing tips and tricks for a successful garden."
        ]
    },
    "mixer_social_Fight_targeted_mean_FatherWinter": {
        "pre_actions": [
            "{initiator} is engaging in a fierce battle with mean Father Winter, fighting for presents!"
        ]
    },
    "mixer_BeeBox_Bond": {
        "pre_actions": [
            "{initiator} is spending time bonding with the bees in the BeeBox."
        ]
    },
    "mixer_BeeBox_MiteTreatment": {
        "pre_actions": [
            "{initiator} is applying mite treatment to the BeeBox to protect against mites."
        ]
    },
    "mixer_BeeBox_Disturb": {
        "pre_actions": [
            "{initiator} is accidentally disturbing the beebox, causing the bees to become agitated and swarm around {target}."
        ]
    },
    "mixer_BeeBox_CollectSwarm": {
        "pre_actions": [
            "{initiator} is approaching the BeeBox to collect a swarm of bees, being careful not to get stung."
        ]
    },
    "mixer_BeeBox_CollectHoney": {
        "pre_actions": [
            "{initiator} is collecting honey from the Bee Box."
        ]
    },
    "mixer_social_Fight_targeted_mean_FlowerBunny": {
        "pre_actions": [
            "{initiator} is engaging in a heated battle with the mean Flower Bunny to claim the Easter eggs."
        ]
    },
    "mixer_BeeBox_SellHoney": {
        "pre_actions": [
            "{initiator} is harvesting honey from the BeeBox and is approaching {target} to sell it to them."
        ]
    },
    "mixer_social_AttemptIntroduction_greetings": {
        "pre_actions": [
            "{initiator} is trying to introduce themselves to {target}, perhaps with a friendly greeting."
        ]
    },
    "mixer_social_FeudBringer_BeginFued_targered_mean_alwaysOn": {
        "pre_actions": [
            "{initiator} is deciding to start a celebrity feud with {target}, targeting them with mean and provocative remarks."
        ]
    },
    "mixer_social_FeudBringer_BlameForFeud_targered_mean_alwaysOn": {
        "pre_actions": [
            "{initiator} is confronting {target} and accusing them of being the one who started the feud."
        ]
    },
    "mixer_social_FeudBringer_EndFeud_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} and declaring an end to the feud between them, in a friendly manner."
        ]
    },
    "mixer_social_WooHooInWalkInSafe_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into a walk-in safe filled with money, and are engaging in a passionate romance transition known as WooHoo."
        ]
    },
    "mixer_social_TryForBabyInWalkInSafe_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into the walk-in safe, covering themselves in a pile of money and transitioning into a romantic moment, trying to conceive a baby."
        ]
    },
    "mixer_social_FamePerk_InstantBesties_FriendlyIntroduction_greetings": {
        "pre_actions": [
            "{initiator}, with their Fame Perk, is instantly becoming best friends with {target} as they are warmly greeting each other."
        ]
    },
    "mixer_social_FamePerk_InstantBesties_RomanceIntroduction_greetings": {
        "pre_actions": [
            "{initiator} is using their fame perk to instantly become besties with {target}, starting off with a romantic introduction and friendly greetings."
        ]
    },
    "mixer_MusicProductionStation_Remix": {
        "pre_actions": [
            "{initiator} is using the Music Production Station to remix a track."
        ]
    },
    "mixer_MusicProductionStation_Idle": {
        "pre_actions": [
            "{initiator} is inviting {target} to collaborate on a music production project together, as both of them are idle and seeking creative opportunities."
        ]
    },
    "mixer_MusicProductionStation_HeadphoneIdles": {
        "pre_actions": [
            "{initiator} is inviting {target} to listen to some music together at the Music Production Station, as they are both idly chatting and enjoying the tunes."
        ]
    },
    "mixer_MusicProductionStation_BurnTrack": {
        "pre_actions": [
            "{initiator} is using the Music Production Station to burn a new track."
        ]
    },
    "mixer_social_Squad_SaySomethingFunny_targered_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} to tell a joke to the squad, hoping to hear something funny."
        ]
    },
    "mixer_social_Squad_TalkMeDown_targered_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is using their friendly approach to talk {target} down and provide support during a challenging situation."
        ]
    },
    "mixer_social_Squad_AskForCompliment_targered_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking for a compliment, hoping to boost their own self-esteem."
        ]
    },
    "mixer_Social_LifestyleBrand_Enthuse": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about {2.String}, showing their enthusiasm for the lifestyle brand."
        ]
    },
    "mixer_Social_LifestyleBrand_Chat": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about their preferred lifestyle brand."
        ]
    },
    "mixer_MusicProductionStation_RemixIdle": {
        "pre_actions": [
            "{initiator} is jumping on the music production station and starting to remix a track while {target} is watching in idle fascination."
        ]
    },
    "mixer_social_Fame_Quirk_ASeriousActor_Targeted_Mean_EmotionSpecific_Rant": {
        "pre_actions": [
            "{initiator}, a famous actor with a serious demeanor, is targeting {target} to express their frustrations about the lack of professionalism in their industry, in a mean and ranting manner."
        ]
    },
    "mixer_social_Fight_targeted_mean_Paparazzi": {
        "pre_actions": [
            "{initiator} is confronting the paparazzi and engaging in a physical altercation, with aggressive and mean intentions."
        ]
    },
    "mixer_socials_TellJoke_group_Funny_alwaysOn_WittyTakedown": {
        "pre_actions": [
            "{initiator} is telling a joke to {target} and the group, leaving everyone in stitches with their funny and witty takedown."
        ]
    },
    "mixer_social_WooHooInSleepingPod_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a romantic interaction, transitioning to WooHoo in the Sleeping Pod."
        ]
    },
    "mixer_social_TryForBabyInSleepingPod_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are getting into a sleeping pod and trying for a baby, marking a special moment in their romantic relationship."
        ]
    },
    "mixer_Dolphin_Pet_autonmous": {
        "pre_actions": [
            "{initiator} is petting the dolphin, who seems to be enjoying the interaction."
        ]
    },
    "mixer_Dolphin_Feed": {
        "pre_actions": [
            "{initiator} is offering a fish to feed the dolphin."
        ]
    },
    "mixer_Dolphin_Dismiss": {
        "pre_actions": [
            "{initiator} is dismissing {target} as if they are just an insignificant dolphin."
        ]
    },
    "mixer_social_Mermaid_AskIfMerfolk_Friendly": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking if they are a mermaid."
        ]
    },
    "mixer_social_Mermaid_AskAboutReaction_Friendly": {
        "pre_actions": [
            "{initiator} is noticing {target}'s strange reaction and is deciding to ask them about it, in a friendly manner."
        ]
    },
    "mixer_social_Mermaid_MerfolkKiss_targeted_alwaysOn": {
        "pre_actions": [
            "{initiator}, a mermaid, is leaning in and kissing {target}, a fellow merfolk, with a magical Mermaid's Kiss."
        ]
    },
    "mixer_social_Mermaid_ImpersonateMerfolk_Mischief_alwaysOn": {
        "pre_actions": [
            "{initiator} is using Mischief to impersonate a mermaid in front of {target}."
        ]
    },
    "mixer_Dolphin_TrickRequest_RubBelly": {
        "pre_actions": [
            "{initiator} is playfully asking {target} if they would like a belly rub, using their trick request to communicate."
        ]
    },
    "mixer_Dolphin_Trick_RubBelly": {
        "pre_actions": [
            "{initiator} is performing a trick and {target} is rewarding them with a belly rub."
        ]
    },
    "mixer_Dolphin_TrickRequest_Dance": {
        "pre_actions": [
            "{initiator} is doing a dolphin trick and inviting {target} to dance together."
        ]
    },
    "mixer_Dolphin_Trick_Dance": {
        "pre_actions": [
            "{initiator} is directing {target}, a trained dolphin, to do a dance."
        ]
    },
    "mixer_Dolphin_TrickRequest_Fetch": {
        "pre_actions": [
            "{initiator} is directing {target}, a trained dolphin, to fetch an object."
        ]
    },
    "mixer_Dolphin_Trick_Fetch": {
        "pre_actions": [
            "{initiator} is throwing a toy for {target} to fetch, and Charlie is eagerly retrieving it as a dolphin trick."
        ]
    },
    "mixer_Dolphin_TrickRequest_Kiss": {
        "pre_actions": [
            "{initiator} is directing {target}, a dolphin, to request a kiss from them."
        ]
    },
    "mixer_Dolphin_Trick_Kiss": {
        "pre_actions": [
            "{initiator} is directing {target}, a dolphin, to give them a kiss."
        ]
    },
    "mixer_Dolphin_Talk": {
        "pre_actions": [
            "{initiator} is engaging in conversation with {target}, a trained dolphin, in an attempt to communicate."
        ]
    },
    "mixer_Dolphin_AskForSquirt": {
        "pre_actions": [
            "{initiator} is playfully asking {target}, a trained dolphin, to squirt water out of their blowhole as a trick."
        ]
    },
    "mixer_social_AskToPlayInIslandWaterfall_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} if they would like to join them in playing in the island waterfall."
        ]
    },
    "mixer_social_TryForBabyInIslandWaterfall_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are deciding to try for a baby by having sex in an island waterfall."
        ]
    },
    "mixer_social_WooHooInIslandWaterfall_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking away to have sex in a secluded island waterfall."
        ]
    },
    "mixer_Dolphin_Pat_userDirected": {
        "pre_actions": [
            "{initiator} is gently patting {target}, a trained dolphin, on its head."
        ]
    },
    "mixer_Dolphin_TrickRequest_Jump": {
        "pre_actions": [
            "{initiator} is asking {target}, a trained dolphin, to perform a jump, wanting to witness their amazing dolphin tricks."
        ]
    },
    "mixer_Dolphin_Trick_Jump": {
        "pre_actions": [
            "{initiator} is directing {target}, a trained dolphin, to perform a jump as an impressive trick."
        ]
    },
    "mixer_Dolphin_SimSplash_Playful": {
        "pre_actions": [
            "{initiator} is playfully splashing {target}, a dolphin, with water."
        ]
    },
    "mixer_Dolphin_SimSplash_Mean": {
        "pre_actions": [
            "{initiator} is spitefully splashing {target}, a dolphin, with water."
        ]
    },
    "mixer_social_Mermaid_KissinWater": {
        "pre_actions": [
            "{initiator}, a mermaid, and {target} are sharing a passionate kiss under the water."
        ]
    },
    "mixer_social_Mermaid_KissinWater_Mermaid": {
        "pre_actions": [
            "{initiator} and {target}, both merfolk, are sharing a magical kiss underwater."
        ]
    },
    "mixer_social_ShareMerfolkLore_target_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly sharing their recent discovery about merfolk lore with {target}, hoping to spark an interesting conversation."
        ]
    },
    "mixer_social_JuiceKeg_AskToDoKegStand_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} in a friendly manner if they want to do a keg stand with some juice."
        ]
    },
    "mixer_social_JuiceKeg_ImTheBest_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is confidently boasting about being the best while enjoying a drink from the Juice Keg. {target} is smiling and responding in a friendly manner."
        ]
    },
    "mixer_social_JuiceKeg_LetsBeFriends_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly offering {target} a drink from the juice keg and suggesting becoming friends."
        ]
    },
    "mixer_social_JuiceKeg_WantToMakeOut_Flirty_alwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} if they want to make out, while both of them are under the influence of the Juice Keg and feeling flirty."
        ]
    },
    "mixer_social_JuiceKeg_CheckThisNoise_Mischief_alwaysOn": {
        "pre_actions": [
            "{initiator} is noticing a strange noise and is excitedly inviting {target} to come investigate with them, eager to uncover the source of the sound."
        ]
    },
    "mixer_social_JuiceKeg_MakeOut_Flirty_AlwaysOn": {
        "pre_actions": [
            "{initiator} is leaning in and giving {target} a passionate kiss, as they are both enjoying the flirty atmosphere from the juice keg."
        ]
    },
    "mixer_CollegeOrganizations_AskToJoinOrQuit": {
        "pre_actions": [
            "{initiator} is politely asking {target} to join a college organization."
        ]
    },
    "mixer_Social_Education_Teach_Fitness": {
        "pre_actions": [
            "{initiator} is taking on the role of a fitness instructor and is teaching {target} about fitness."
        ]
    },
    "mixer_Social_Education_AskDonation": {
        "pre_actions": [
            "{initiator} is approaching {target} and politely asking for a donation to support the university's educational programs."
        ]
    },
    "mixer_Social_Education_AskVolunteer": {
        "pre_actions": [
            "{initiator} is asking {target} if they would like to volunteer their time for an educational cause."
        ]
    },
    "mixer_Social_Education_Teach_Handiness": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} to educate them about handiness skills."
        ]
    },
    "mixer_Social_Education_Teach_Research": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} to educate them about research and debate."
        ]
    },
    "mixer_Social_Education_Teach_Writing": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target} to educate them about writing."
        ]
    },
    "mixer_Social_Education_Teach_Programming": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target} to teach them about programming."
        ]
    },
    "mixer_Social_Education_Teach_Robotics": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} to teach them about robotics."
        ]
    },
    "mixer_Social_Education_Teach_RocketScience": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target}, attempting to teach them about rocket science."
        ]
    },
    "mixer_Social_Education_Teach_Videogaming": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target} to educate them about video gaming."
        ]
    },
    "mixer_Social_Education_Teach_Acting": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target} to educate them about the art of acting."
        ]
    },
    "mixer_Social_Education_Teach_Charisma": {
        "pre_actions": [
            "{initiator} is teaching {target} about charisma, sharing tips and tricks to improve their social skills."
        ]
    },
    "mixer_Social_Education_Teach_Comedy": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target}, teaching them about comedy."
        ]
    },
    "mixer_Social_Education_Teach_Painting": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target} in order to teach them about painting."
        ]
    },
    "mixer_Social_Education_Teach_Cooking": {
        "pre_actions": [
            "{initiator} is taking the opportunity to teach {target} about cooking, sharing their knowledge and tips."
        ]
    },
    "mixer_Social_Education_Teach_Gardening": {
        "pre_actions": [
            "{initiator} is taking the opportunity to educate {target} about the art of gardening."
        ]
    },
    "mixer_Social_Education_Teach_Logic": {
        "pre_actions": [
            "{initiator} is taking the opportunity to teach {target} about logic, engaging in a social and educational interaction."
        ]
    },
    "mixer_Social_Education_Teach_Photography": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target} to educate and teach them about photography."
        ]
    },
    "mixer_Social_DiscussStrategy_Targeted_Friendly_AlwaysOn_SoccerTeam": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, discussing soccer strategies, aimed at their shared interest in the sport."
        ]
    },
    "mixer_CollegeOrganizations_AskToJoinOrQuit_Art": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking to join the College Art Society."
        ]
    },
    "mixer_CollegeOrganizations_AskToJoinOrQuit_Debate": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking if they can join the Debate Guild, knowing that {target} is involved in college organizations."
        ]
    },
    "mixer_CollegeOrganizations_AskToJoinOrQuit_Honor": {
        "pre_actions": [
            "{initiator} is asking {target} if they would like to join The Brainiacs, a college organization known for its academic prowess and dedication to honor."
        ]
    },
    "mixer_CollegeOrganizations_AskToJoinOrQuit_Prank": {
        "pre_actions": [
            "{initiator} is asking {target} if they would like to join the Britechester Spirit Corps, a college organization known for their pranks."
        ]
    },
    "mixer_CollegeOrganizations_AskToJoinOrQuit_Robotics": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking if they can join the Bot Savants, an organization focused on robotics, possibly because of their interest in college."
        ]
    },
    "mixer_social_DiscussFavoriteArtPieces_targeted_Friendly_alwaysOn_STC": {
        "pre_actions": [
            "{initiator} is initiating a friendly conversation with {target} to discuss their favorite art pieces."
        ]
    },
    "mixer_social_YellAT_targeted_mean_StudentCommons_GrumpyProfessor": {
        "pre_actions": [
            "{initiator} is yelling at {target} angrily in the Student Commons, possibly because {initiator} is being a grumpy professor."
        ]
    },
    "mixer_social_CollegeOrganizations_SchoolSpirit_Prank_AskToPaint": {
        "pre_actions": [
            "{initiator} is encouraging {target} to paint murals as part of a college organization's initiative to promote school spirit and pull off a prank."
        ]
    },
    "mixer_social_DiscussPaintingStyle_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} to discuss their painting style."
        ]
    },
    "mixer_social_AskToBeBoyfriend_targeted_romance_relationship_RoommateNPC": {
        "pre_actions": [
            "{initiator} is mustering up the courage to ask {target} if they want to take their relationship to the next level and become boyfriends."
        ]
    },
    "mixer_social_AskToBeGirlfriend_targeted_romance_relationship_RoommateNPC": {
        "pre_actions": [
            "{initiator} is mustering up the courage to ask {target} if they would like to become their official girlfriend and take their relationship to the next level."
        ]
    },
    "mixer_social_CollegeOrganizations_SchoolSpirit_Prank_HeckleArtsMascot": {
        "pre_actions": [
            "{initiator} is joining a group of college students at a school spirit event and playfully heckling the arts mascot."
        ]
    },
    "mixer_social_CollegeOrganizations_SchoolSpirit_Prank_HeckleScienceMascot": {
        "pre_actions": [
            "{initiator} is playfully heckling the college mascot, showing off their school spirit and adding some humor to the atmosphere."
        ]
    },
    "mixer_social_CollegeOrganizations_SchoolSpirit_Prank_TellJokeAboutScienceUniversity": {
        "pre_actions": [
            "{initiator} is telling a joke about Foxbury Institute to {target}, sparking a playful conversation about college organizations and school spirit."
        ]
    },
    "mixer_social_AskAboutInspiration_Friendly": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking about their inspiration, hoping to gain some creative insight."
        ]
    },
    "mixer_social_DiscussScrapCollectionStrategy_targeted_friendly": {
        "pre_actions": [
            "{initiator} and {target} are having a friendly discussion about their scrap collection strategy."
        ]
    },
    "mixer_social_EnthuseAboutRobotics_targeted_friendly": {
        "pre_actions": [
            "{initiator} is enthusiastically talking to {target} about robotics, sharing their knowledge and passion for the subject."
        ]
    },
    "mixer_social_DiscussFavoriteBots_targeted_friendly": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a friendly discussion about their favorite Utili-Bots."
        ]
    },
    "mixer_social_Friendly_CollegeOrganizations_Debate_DiscussDebate": {
        "pre_actions": [
            "{initiator} is engaging in a friendly debate with {target} about college organizations."
        ]
    },
    "mixer_social_Friendly_CollegeOrganizations_Debate_Inquire": {
        "pre_actions": [
            "{initiator} is asking {target} about their debate strategy, as they are both members of college debate organizations."
        ]
    },
    "mixer_social_Friendly_CollegeOrganizations_Debate_OfferFeedback": {
        "pre_actions": [
            "{initiator} is approaching {target} after a debate and is offering friendly feedback on their performance in the debate, as members of the same college organization."
        ]
    },
    "mixer_social_SchoolSpirit_Prank_greetings": {
        "pre_actions": [
            "{initiator} is enthusiastically greeting {target} with a playful prank, showcasing their school spirit."
        ]
    },
    "mixer_social_Fight_targeted_mean_Mascot": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated fight, fueled by their mean and Mascot traits."
        ]
    },
    "mixer_social_SchoolSpirit_Party_greetings": {
        "pre_actions": [
            "{initiator}, filled with school spirit, is greeting {target} at the party."
        ]
    },
    "mixer_social_CollegeOrganizations_SchoolSpirit_Prank_ThrowConfetti": {
        "pre_actions": [
            "{initiator} is engaging in a spirited prank with {target}, throwing confetti in celebration of their college organizations and school spirit."
        ]
    },
    "mixer_Social_E-Sports_DiscussStrategies": {
        "pre_actions": [
            "{initiator} is engaging in a discussion with {target} to share and learn strategies to improve their SimScuffle performance in the world of e-sports."
        ]
    },
    "mixer_Social_E-Sports_ComplimentSkills": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their impressive SimScuffle skills, recognizing their talent in the field of E-Sports."
        ]
    },
    "mixer_Social_UniversityRivalry_TauntAboutUniversitySuperiority": {
        "pre_actions": [
            "{initiator} is confronting {target} about the superiority of their university, taunting them in a competitive manner."
        ]
    },
    "mixer_CollegeOrganizations_AskToJoinOrQuit_Party": {
        "pre_actions": [
            "{initiator} is approaching {target}, a member of the Foxbury Spirit Squad, and is asking if they can join the college organization. They are mentioning that they love to party and would be a great addition to the team."
        ]
    },
    "mixer_social_TryForBabyInShower_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into the shower together, hoping to start a family."
        ]
    },
    "mixer_social_WooHooInShower_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a romantic WooHoo session together in the shower."
        ]
    },
    "mixer_social_ProfessOnFabrication_targetted_friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} is taking {target} aside and excitedly talking about the wonders of fabrication, sharing their passion and knowledge."
        ]
    },
    "mixer_Social_CivicPolicy_ConvinceToSupportPolicy": {
        "pre_actions": [
            "{initiator} is engaging in a social conversation with {target} in an attempt to convince them to support a specific civic policy."
        ]
    },
    "mixer_Social_CivicPolicy_ConvinceToInstall_Recycler": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target}, trying to convince them to buy a recycler for their home as part of the civic policy."
        ]
    },
    "mixer_Social_CivicPolicy_RepealPolicy_GetSignature": {
        "pre_actions": [
            "{initiator} is approaching {target} and politely asking if they would be willing to sign a petition to repeal a certain policy."
        ]
    },
    "mixer_Social_CivicPolicy_ConvinceToInstall_Fabricator": {
        "pre_actions": [
            "{initiator} is engaging in a social conversation with {target}, trying to convince them to buy and install a fabricator for civic policy reasons."
        ]
    },
    "mixer_social_TryForBabyInDumpster_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a romantic interaction and trying for a baby in a dumpster."
        ]
    },
    "mixer_social_WooHooInDumpster_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} is suggesting to {target} that they are diving into a dumpster for an adventurous thrill. This is potentially leading to a romantic encounter or transitioning into a more intimate relationship."
        ]
    },
    "mixer_Social_RecyclingGuru_AskForTips": {
        "pre_actions": [
            "{initiator} is approaching {target}, who is known as the Recycling Guru, and is asking for some recycling tips."
        ]
    },
    "mixer_Social_RecyclingGuru_AskForMaterials": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking if they have any extra recycling materials to spare, as they are known to be a recycling guru."
        ]
    },
    "mixer_social_Fight_targeted_mean_CommunityCloseness": {
        "pre_actions": [
            "{initiator} is forcefully arguing with {target} in order to end their association, displaying hostility and a lack of community closeness."
        ]
    },
    "mixer_Social_CivicPolicy_ConvinceToInstall_GreenGardening_BeeBox": {
        "pre_actions": [
            "{initiator} is educating {target} about the benefits of installing a Bee Box as part of a green gardening initiative."
        ]
    },
    "mixer_Social_CivicPolicy_ConvinceToInstall_GreenGardening_InsectFarm": {
        "pre_actions": [
            "{initiator} is trying to convince {target} to install an insect farm as part of a green gardening initiative."
        ]
    },
    "mixer_Social_CivicPolicy_ConvinceToInstall_GreenGardening_Planter": {
        "pre_actions": [
            "{initiator} is approaching {target} to discuss civic policies and is convincing them to install planters for green gardening."
        ]
    },
    "mixer_Social_CivicPolicy_ConvinceToInstall_GreenGardening_VerticalGarden": {
        "pre_actions": [
            "{initiator} is discussing the benefits of installing a vertical garden with {target}, in an effort to convince them to adopt green gardening practices and implement a vertical garden."
        ]
    },
    "mixer_Social_CivicPolicy_ConvinceToInstall_UtilityProduction_DewCollector": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target}, convincing them to install a dew collector for utility production as part of the civic policy."
        ]
    },
    "mixer_Social_CivicPolicy_ConvinceToInstall_UtilityProduction_SolarPanel": {
        "pre_actions": [
            "{initiator} is discussing the benefits of installing solar panels with {target} as part of a civic policy to promote utility production."
        ]
    },
    "mixer_Social_CivicPolicy_ConvinceToInstall_UtilityProduction_WindTurbine": {
        "pre_actions": [
            "{initiator} is discussing the benefits of installing wind turbines with {target}, in order to convince them to consider implementing them for utility production."
        ]
    },
    "mixer_Social_CivicPolicy_BragAbout_Beebox": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} about their new bee box, highlighting the benefits of having bees and how it aligns with their civic policy."
        ]
    },
    "mixer_Social_CivicPolicy_BragAbout_WindTurbine": {
        "pre_actions": [
            "{initiator} is enthusiastically discussing the benefits of wind turbines with {target}, showing off their knowledge on the topic."
        ]
    },
    "mixer_Social_CivicPolicy_BragAbout_SolarPanel": {
        "pre_actions": [
            "{initiator} is engaging in a social conversation with {target} and is taking the opportunity to brag about their solar panel installation."
        ]
    },
    "mixer_Social_CivicPolicy_BragAbout_DewCollector": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target} where they are proudly bragging about their implementation of the Dew Collector civic policy."
        ]
    },
    "mixer_Social_CivicPolicy_BragAbout_Recycler": {
        "pre_actions": [
            "{initiator} is engaging in a persuasive conversation with {target}, emphasizing the benefits of buying a recycler and how it aligns with their civic policies. They are also proudly mentioning their own use of a recycler."
        ]
    },
    "mixer_Social_CivicPolicy_BragAbout_Fabricator": {
        "pre_actions": [
            "{initiator} is trying to convince {target} to buy a fabricator, while bragging about its benefits and discussing how it aligns with their civic policy."
        ]
    },
    "mixer_Social_CivicPolicy_BragAbout_VerticalGarden": {
        "pre_actions": [
            "{initiator} is enthusiastically showing off their impressive vertical garden to {target}, while also discussing the benefits of incorporating more green spaces in the city."
        ]
    },
    "mixer_Social_CivicPolicy_BragAbout_Planter": {
        "pre_actions": [
            "{initiator} is approaching {target} and is starting to brag about their impressive collection of planters. They are discussing their passion for gardening and the civic policy related to urban planting."
        ]
    },
    "mixer_Social_CivicPolicy_BragAbout_InsectFarm": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their successful insect farm, bragging about their insect collection and discussing the benefits of implementing insect farming as a civic policy."
        ]
    },
    "mixer_Social_ShareIdeasAboutMaking_targetted_friendly_NPCOnly": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target} about crafting, exchanging ideas and tips."
        ]
    },
    "mixer_social_Fight_targeted_CivicPolicy_Aggression": {
        "pre_actions": [
            "{initiator} is initiating a fight with {target}, expressing their aggression and disregard for civic policy."
        ]
    },
    "mixer_social_Fight_targeted_CivicPolicy_Aggression_Transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument, fueled by differing opinions on civic policy. The conversation is quickly escalating into a physical fight."
        ]
    },
    "mixer_social_Targeted_Romance_CivicPolicy_FreeLove_NT_AskRisqueQuestion": {
        "pre_actions": [
            "{initiator} is boldly asking {target} a risqué question, pushing the boundaries of their conversation."
        ]
    },
    "mixer_social_Targeted_Romance_CivicPolicy_FreeLove_NT_BlowAKiss": {
        "pre_actions": [
            "{initiator} is blowing a kiss towards {target}, expressing their romantic feelings."
        ]
    },
    "mixer_social_Targeted_Romance_CivicPolicy_FreeLove_T_CaressCheek": {
        "pre_actions": [
            "{initiator} is gently caressing {target}'s cheek, expressing a romantic and affectionate gesture."
        ]
    },
    "mixer_social_Targeted_Romance_CivicPolicy_FreeLove_T_Embrace": {
        "pre_actions": [
            "{initiator} is passionately embracing {target} as a romantic gesture, expressing their love and support. Their embrace is representing their belief in free love and their commitment to the civic policy of embracing all forms of love equally."
        ]
    },
    "mixer_social_Targeted_Romance_CivicPolicy_FreeLove_NT_Flirt": {
        "pre_actions": [
            "{initiator} is targeting {target} and using flirtatious comments to express romantic interest, in accordance with the Free Love civic policy and the concepts of non-traditional romance."
        ]
    },
    "mixer_social_Targeted_Romance_CivicPolicy_FreeLove_T_HoldHands": {
        "pre_actions": [
            "{initiator} is reaching out to {target} and suggesting holding hands, expressing their affection and closeness."
        ]
    },
    "mixer_social_Targeted_Romance_CivicPolicy_FreeLove_T_KissNeck": {
        "pre_actions": [
            "{initiator} is passionately kissing {target}'s neck, expressing their love and affection in a moment of intimacy."
        ]
    },
    "mixer_social_Targeted_Romance_CivicPolicy_FreeLove_T_OfferMassage": {
        "pre_actions": [
            "{initiator} is offering to give {target} a relaxing massage, as an expression of their affection."
        ]
    },
    "mixer_social_Targeted_Romance_CivicPolicy_FreeLove_T_WhisperSeductively": {
        "pre_actions": [
            "{initiator} is leaning in close to {target} and whispering seductively, enticing them with their romantic charm."
        ]
    },
    "mixer_Social_Skiing_InquireAboutPowderConditions_Friendly_NT": {
        "pre_actions": [
            "{initiator} is asking {target} about the current conditions on the slopes, curious about the quality of the powder for skiing."
        ]
    },
    "mixer_Social_Skiing_DeliberateSkiStyle_Friendly_NT": {
        "pre_actions": [
            "{initiator} and {target} are discussing their favorite ski styles and are deliberating on the technique they use while skiing, in a friendly and non-threatening manner."
        ]
    },
    "mixer_Social_Skiing_GiveAdviceOnAvoidingWipeouts_Friendly_NT": {
        "pre_actions": [
            "{initiator} is offering some friendly advice to {target} on how to avoid wipeouts while skiing."
        ]
    },
    "mixer_Socials_RevokeSnowBro_Targeted_Friendly_Snowboarding": {
        "pre_actions": [
            "{initiator} is playfully revoking {target}'s 'Snow Bro' status during a friendly conversation about snowboarding."
        ]
    },
    "mixer_socials_EndureTheBurn_Targeted_Friendly_Snowboarding": {
        "pre_actions": [
            "{initiator} is bravely encouraging {target} to endure the burn while they are snowboarding together, showcasing their friendly and supportive side."
        ]
    },
    "mixer_socials_BragAboutShredding_Targeted_Friendly_Snowboarding": {
        "pre_actions": [
            "{initiator} is excitedly bragging to {target} about their shredding skills on the slopes, bonding over their shared love for snowboarding."
        ]
    },
    "mixer_socials_DareToAttemptRiskySlope_Targeted_Mischief_Snowboarding": {
        "pre_actions": [
            "{initiator} is daring {target} to attempt a risky slope while snowboarding, adding a touch of mischief to their interaction."
        ]
    },
    "mixer_socials_ChatAboutRadSlope_Targeted_Friendly_Snowboarding": {
        "pre_actions": [
            "{initiator} is initiating a friendly conversation with {target} and chatting about rad slopes, bonding over their shared love for snowboarding."
        ]
    },
    "mixer_socials_Coach_Targeted_Friendly_Snowboarding": {
        "pre_actions": [
            "{initiator} is offering to coach {target} in the art of snowboarding, providing guidance and support."
        ]
    },
    "mixer_socials_ProvideTips_Targeted_Friendly_Snowboarding": {
        "pre_actions": [
            "{initiator} is offering {target} some friendly snowboarding tips during their conversation."
        ]
    },
    "mixer_Social_Skiing_CoachSimNameInSkiing_Friendly_NT": {
        "pre_actions": [
            "{initiator} is offering to coach {target} in skiing, providing guidance and support to help them improve their skills on the slopes."
        ]
    },
    "mixer_Social_Skiing_OfferSkiExpertise_NPCSims_Friendly_NT": {
        "pre_actions": [
            "{initiator} is offering their expertise in skiing to {target}, hoping to help them improve their skills on the slopes."
        ]
    },
    "mixer_Social_Skiing_OfferSkiExpertise_HHSims_Friendly_NT": {
        "pre_actions": [
            "{initiator} is offering to share their skiing expertise with {target} for free, in a friendly and helpful manner."
        ]
    },
    "mixer_Lifestyles_FrequentTraveler_ShareTravelStories_Listening": {
        "pre_actions": [
            "{initiator} and {target} are discussing their careers, sharing stories about their frequent travels and listening to each other's experiences."
        ]
    },
    "mixer_Social_Skiing_OfferSkiExpertise_Continued_Friendly_NT": {
        "pre_actions": [
            "{initiator} is offering their ski expertise to {target} in a friendly and ongoing conversation."
        ]
    },
    "mixer_Lifestyles_FrequentTraveler_AskAboutHomeRegion": {
        "pre_actions": [
            "{initiator} is inquiring about {target}'s home region, curious to learn more about their travels and lifestyle."
        ]
    },
    "mixer_Social_Skiing_DiscussPastSkiExperiences_Friendly_NT": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a friendly conversation about their past skiing experiences."
        ]
    },
    "mixer_Social_Lifestyles_CoffeeFanatic_TalkAboutCoffee_Positive": {
        "pre_actions": [
            "{initiator} is engaging {target} in a conversation about the benefits of coffee, discussing their shared interest in the topic."
        ]
    },
    "mixer_Social_Lifestyles_CoffeeFanatic_TalkAboutCoffee_Negative": {
        "pre_actions": [
            "{initiator} is expressing their displeasure with the negative effects of coffee to {target}, who is a coffee fanatic."
        ]
    },
    "mixer_Social_AskToBeConfidant": {
        "pre_actions": [
            "{initiator} is asking {target} if they can be their confidant, seeking a deeper level of trust and intimacy in their relationship."
        ]
    },
    "mixer_social_WooHooInHotSprings_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking off to the hot springs for a steamy night of romance, transitioning into a passionate woohoo session."
        ]
    },
    "mixer_social_TryForBabyInHotSprings_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sharing a romantic moment in the hot springs, trying to start a family together."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_Techie": {
        "pre_actions": [
            "{initiator} is sharing some techie tips with {target}, discussing their knowledge and expertise in the tech field."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_Technophobe": {
        "pre_actions": [
            "{initiator}, who is a technophobe, is sharing tips with {target} about how to avoid technology."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_Workaholic": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target}, sharing tips on how to balance work and personal life as a workaholic."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_FrequentTravleer": {
        "pre_actions": [
            "{initiator} is initiating a conversation with {target} to share tips for frequent travelers."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_Sedentary": {
        "pre_actions": [
            "{initiator} is sharing sedentary tips with {target}, discussing ways to stay comfortable and relax while leading a less active lifestyle."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_Energetic": {
        "pre_actions": [
            "{initiator} is sharing some energetic tips with {target} during their conversation about lifestyles."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_Indoorsy": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target} to share tips and advice on living an indoorsy lifestyle."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_Outdoorsy": {
        "pre_actions": [
            "{initiator}, who loves being outdoors, is sharing outdoorsy lifestyle tips with {target}."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_CloseKnit": {
        "pre_actions": [
            "{initiator}, who enjoys close-knit relationships, is sharing tips with {target} about their lifestyle."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_Networker": {
        "pre_actions": [
            "{initiator}, an avid networker, is sharing some tips with {target} on how to connect with people."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_JunkFood": {
        "pre_actions": [
            "{initiator} and {target} are sharing tips on indulging in their love for junk food, bonding over their similar lifestyles."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_HealthNut": {
        "pre_actions": [
            "{initiator} and {target} are having a social interaction where they are sharing health food nut tips to promote a healthier lifestyle."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_NoRomance": {
        "pre_actions": [
            "{initiator} is sharing some tips on enjoying being single with {target}, emphasizing the importance of embracing the single lifestyle without any romantic involvement."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_HungryLove": {
        "pre_actions": [
            "{initiator} is engaging in a social conversation with {target}, sharing helpful tips and advice on how to find love when feeling hungry for it."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_AdrenalineJunkie": {
        "pre_actions": [
            "{initiator} is excitedly sharing adrenaline seeker tips with {target}, discussing their adventurous lifestyle."
        ]
    },
    "mixer_Social_Lifestyles_ShareLifestyleTips_CoffeeFanatic": {
        "pre_actions": [
            "{initiator} is engaging in a social interaction with {target}, sharing coffee fanatic tips and discussing their shared passion for coffee."
        ]
    },
    "mixer_Social_Lifestyles_Techie_EnthuseAboutProcessingPower": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target}, enthusiastically discussing their passion for processing power."
        ]
    },
    "mixer_Social_Lifestyles_Technophobe_ComplainAboutTechnology": {
        "pre_actions": [
            "{initiator} is expressing their frustration about the technological apocalypse to {target}, who might be sharing their dislike for technology."
        ]
    },
    "mixer_Social_Lifestyles_Technophobe_InsultRoboticExistence": {
        "pre_actions": [
            "{initiator} is openly expressing their dislike for {target}'s mechanical existence, insulting their robotic nature and lifestyle choices."
        ]
    },
    "mixer_Social_Lifestyles_Technophobe_ThreatenRobotUprising": {
        "pre_actions": [
            "{initiator} is confronting {target}, expressing their fear and disapproval of technology and warning about a potential robot uprising."
        ]
    },
    "mixer_social_Targeted_TalkAboutNewAdventure_Lifestyles_AdrenalineSeeker": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target}, specifically discussing their love for new adventures and seeking out adrenaline-filled experiences."
        ]
    },
    "mixer_social_Fight_targeted_mean_Lifestyles_AdrenalineSeeker": {
        "pre_actions": [
            "{initiator} is challenging {target} to a fight, fueled by their competitive and thrill-seeking nature."
        ]
    },
    "mixer_social_RespectfulIntroduction_greetings": {
        "pre_actions": [
            "{initiator} is approaching {target} with a respectful greeting, introducing themselves politely."
        ]
    },
    "mixer_social_WooHoo_targeted_romance_transition_InteractableCave": {
        "pre_actions": [
            "{initiator} and {target} are sneaking off to a hidden cave for a romantic rendezvous, engaging in some intimate WooHoo."
        ]
    },
    "mixer_social_TryForBabyInCave_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking away to a private cave and trying for a baby, taking their relationship to the next level."
        ]
    },
    "mixer_social_TreadMill_Rock_ClimbingWall_BragAboutBeatingHighScore_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} about their recent achievement of beating a climbing time on the rock climbing wall at the gym."
        ]
    },
    "mixer_social_TreadMill_Rock_ClimbingWall_BragAbout_ClimbingProwess_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is proudly boasting about their impressive climbing skills to {target}, showing off their strength and agility."
        ]
    },
    "mixer_social_Laundry_Targeted_EmotionSpecific_SmellGood": {
        "pre_actions": [
            "{initiator} is exploring {target}'s fresh laundry, taking a moment to sniff the clothes and enjoy the pleasant scent."
        ]
    },
    "mixer_social_Laundry_Targeted_EmotionSpecific_SmellFoul": {
        "pre_actions": [
            "{initiator} is approaching {target} and taking a sniff of their foul-smelling laundry."
        ]
    },
    "mixer_social_Targeted_Friendly_MiddleScore_STC_WhatsThatSpot_Child": {
        "pre_actions": [
            "{initiator} is noticing a spot on {target}'s clothing and is approaching them in a friendly manner to inquire about it."
        ]
    },
    "mixer_social_Targeted_Friendly_AlwaysOn_STC_AskAbout_RodentDisease": {
        "pre_actions": [
            "{initiator} is approaching {target} in a friendly manner and asking about Rabid Rodent Fever."
        ]
    },
    "mixer_social_BragAboutTinyHome": {
        "pre_actions": [
            "{initiator} is proudly showing off their small home to {target}, bragging about how cozy and efficient it is."
        ]
    },
    "mixer_social_Knitting_ShowOff": {
        "pre_actions": [
            "{initiator} is proudly showing off their knitted clothing to {target}, displaying their knitting skills."
        ]
    },
    "mixer_social_YellAT_targeted_mean_Knitting_SweaterCurse": {
        "pre_actions": [
            "{initiator} is angrily yelling at {target} while they are knitting a sweater, using mean and curse words."
        ]
    },
    "mixer_social_Mean_Dust_DemandClean": {
        "pre_actions": [
            "{initiator} is ordering {target} to clean, in a demanding and mean tone."
        ]
    },
    "mixer_social_Mean_Dust_Argue": {
        "pre_actions": [
            "{initiator} is confronting {target} about the dirty surroundings, resulting in an argument."
        ]
    },
    "mixer_Social_Dust_AskClean": {
        "pre_actions": [
            "{initiator} is politely asking {target} for help with cleaning, as there is a lot of dust around."
        ]
    },
    "mixer_social_TryForBabyInLivestockPen_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into the animal shed together, hoping to start a family."
        ]
    },
    "mixer_social_WooHooInLivestockPen_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking off to the animal shed for a secret rendezvous, engaging in a passionate WooHoo session."
        ]
    },
    "mixer_social_CottageWorld_NPC_GossipAboutVillage_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is taking {target} aside in the charming village of Henford-on-Bagley to have a heart-to-heart conversation about the happenings in the village."
        ]
    },
    "mixer_AnimalEnthusiastTrait_DiscussIfChicken": {
        "pre_actions": [
            "{initiator} with the Animal Enthusiast Trait is engaging in a discussion with {target} about the age-old question of whether the chicken or the egg came first."
        ]
    },
    "mixer_AnimalEnthusiastTrait_ShareDelight": {
        "pre_actions": [
            "{initiator}, an animal enthusiast, is excitedly sharing their delight about animals with {target}."
        ]
    },
    "mixer_AnimalEnthusiastTrait_MopeMissingAnimals": {
        "pre_actions": [
            "{initiator}, an Animal Enthusiast, is sadly moping about the missing animals with {target}."
        ]
    },
    "mixer_LactoseIntolerantTrait_ComplainAboutBloating": {
        "pre_actions": [
            "{initiator}, who is lactose intolerant, is complaining to {target} about feeling bloated after consuming dairy products."
        ]
    },
    "mixer_LactoseIntolerantTrait_ShareWondersOfDairyFree": {
        "pre_actions": [
            "{initiator} with the Lactose Intolerant Trait is sharing the wonders of living a dairy-free life with {target}."
        ]
    },
    "mixer_LactoseIntolerantTrait_TheorizeAboutMilkyWay": {
        "pre_actions": [
            "{initiator}, who is lactose intolerant, is engaging in a lively conversation with {target} about their shared interest in theorizing about the Milky Way conspiracy."
        ]
    },
    "mixer_Social_HighSchool_Active_GetClassList": {
        "pre_actions": [
            "{initiator} is asking {target} about their new school, hoping to learn more about it. They are discussing classes and activities that are available."
        ]
    },
    "mixer_Social_HighSchool_Active_TalkToTeacher": {
        "pre_actions": [
            "{initiator} is initiating a conversation with {target} to discuss the curriculum."
        ]
    },
    "mixer_social_Targeted_Mean_AlwaysOn_Teens_MockRival": {
        "pre_actions": [
            "{initiator} is purposely targeting {target} and engaging in mean-spirited behavior, mocking them as a rival."
        ]
    },
    "mixer_social_ConvinceToJoinTeam_Targeted_Friendly_AlwaysOn_Teens": {
        "pre_actions": [
            "{initiator} is approaching {target} and using their friendly and persuasive skills to convince them to join their team."
        ]
    },
    "mixer_Social_HighSchoolFestival_TauntRival": {
        "pre_actions": [
            "{initiator} is attending the High School Festival and is deciding to taunt {target}, their rival, in a social interaction."
        ]
    },
    "mixer_Social_Fight_HighSchool_Active_SchoolFight": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated fight at the high school, causing a scene and attracting attention from others."
        ]
    },
    "mixer_Social_BedUpdates_AskToPillowFight": {
        "pre_actions": [
            "{initiator} is playfully challenging {target} to a pillow fight, asking them to indulge in some friendly fun on the bed."
        ]
    },
    "mixer_Social_Targeted_Friendly_OpenableWindow_AskForPermission": {
        "pre_actions": [
            "{initiator} is politely approaching {target} and asking for permission to go to an event."
        ]
    },
    "mixer_social_HighSchoolFestival_RequestScienceFair": {
        "pre_actions": [
            "{initiator} is approaching {target} at the High School Festival and is requesting them to participate in the Science Fair."
        ]
    },
    "mixer_HighSchool_Active_HSExit_Principal_Dropout": {
        "pre_actions": [
            "{initiator} is deciding to drop out of high school and is informing the principal of their decision."
        ]
    },
    "mixer_HighSchool_Active_HSExit_Principal_GraduateEarly": {
        "pre_actions": [
            "{initiator} is successfully completing all their high school requirements and is receiving approval from the principal to graduate early."
        ]
    },
    "mixer_social_Targeted_Friendly_SetExpectations": {
        "pre_actions": [
            "{initiator} is having a friendly conversation with {target}, discussing their expectations for the future."
        ]
    },
    "mixer_social_Overachiever_HumbleBrag": {
        "pre_actions": [
            "{initiator} is subtly boasting about their many achievements to {target} while maintaining a modest demeanor."
        ]
    },
    "mixer_social_Overachiever_AskforExtraCredit": {
        "pre_actions": [
            "{initiator}, the overachiever, is asking {target} for extra, extra credit."
        ]
    },
    "mixer_social_Overachiever_EnthuseAboutLearning": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about learning additional skills, showing their overachiever spirit."
        ]
    },
    "mixer_social_PartyAnimal_EnthuseAboutParties": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their love for parties, gushing about the fun and excitement they bring."
        ]
    },
    "mixer_social_PartyAnimal_VibeCheck": {
        "pre_actions": [
            "{initiator} is initiating a vibe check with {target}, to see if they are bringing the party energy."
        ]
    },
    "mixer_social_PartyAnimal_TalkAboutPastParties": {
        "pre_actions": [
            "{initiator} is excitedly discussing past parties with {target}, showcasing their party animal side."
        ]
    },
    "mixer_social_Targeted_TeenPranks_UrbanMyth": {
        "pre_actions": [
            "{initiator} is playing a prank on {target}, telling them an urban myth specifically targeted at teens."
        ]
    },
    "mixer_Shower_Shave_Arms": {
        "pre_actions": [
            "{initiator} is hopping into the shower and proceeding to shave their arm hair."
        ]
    },
    "mixer_Shower_Shave_Face": {
        "pre_actions": [
            "{initiator} is lathering up in the shower and proceeding to carefully shave off their facial hair."
        ]
    },
    "mixer_Shower_Shave_Legs": {
        "pre_actions": [
            "{initiator} is taking a shower and then proceeding to shave their leg hair."
        ]
    },
    "mixer_Shower_Shave_Torso": {
        "pre_actions": [
            "{initiator} is taking a shower and deciding to shave their chest hair."
        ]
    },
    "mixer_Shower_Shave_Arms_Passive": {
        "pre_actions": [
            "{initiator} is deciding to shave their arm hair while taking a shower, using a passive approach."
        ]
    },
    "mixer_Shower_Shave_Face_Passive": {
        "pre_actions": [
            "{initiator} is taking a shower and shaving their face, in a passive manner."
        ]
    },
    "mixer_Shower_Shave_Legs_Passive": {
        "pre_actions": [
            "{initiator} is in the shower and is casually shaving their legs."
        ]
    },
    "mixer_Shower_Shave_Torso_Passive": {
        "pre_actions": [
            "{initiator} is shaving their chest hair while they are taking a shower, concentrating on the torso area, in a serene and passive manner."
        ]
    },
    "mixer_HSGraduation_AskAboutGraduation": {
        "pre_actions": [
            "{initiator} is asking {target} about their graduation from high school."
        ]
    },
    "mixer_HSGraduation_ReminisceAboutSchoolYear": {
        "pre_actions": [
            "{initiator} and {target} are taking a moment to reminisce about their high school graduation and the memories from their school year."
        ]
    },
    "mixer_HSGraduation_Congratulate": {
        "pre_actions": [
            "{initiator} is congratulating {target} on their high school graduation."
        ]
    },
    "mixer_HSGraduation_FakeCongratulate": {
        "pre_actions": [
            "{initiator} is sarcastically congratulating {target} on their high school graduation."
        ]
    },
    "mixer_HSGraduation_ThankForSchoolYear": {
        "pre_actions": [
            "{initiator} is expressing gratitude to {target} for their support throughout the school year."
        ]
    },
    "mixer_Shower_Shave_Torso_Preferred": {
        "pre_actions": [
            "{initiator} is going to the shower and shaving the hair on their torso to their preferred length."
        ]
    },
    "mixer_Shower_Shave_Torso_Preferred_Passive": {
        "pre_actions": [
            "{initiator} is entering the shower and proceeding to shave their chest hair to their preferred length in a passive manner."
        ]
    },
    "mixer_Shower_Shave_Legs_Preferred": {
        "pre_actions": [
            "{initiator} is stepping into the shower and carefully shaving their leg hair to their preferred length."
        ]
    },
    "mixer_Shower_Shave_Legs_Preferred_Passive": {
        "pre_actions": [
            "{initiator} is taking a shower and shaving their leg hair to their preferred length."
        ]
    },
    "mixer_Shower_Shave_Face_Preferred": {
        "pre_actions": [
            "{initiator} is taking a shower and then shaving their face to their preferred length."
        ]
    },
    "mixer_Shower_Shave_Face_Preferred_Passive": {
        "pre_actions": [
            "{initiator} is using the shower to shave {initiator's} facial hair to the preferred length in a passive manner."
        ]
    },
    "mixer_Shower_Shave_Arms_Preferred": {
        "pre_actions": [
            "{initiator} is taking a shower and deciding to shave their arm hair to their preferred length."
        ]
    },
    "mixer_Shower_Shave_Arms_Preferred_Passive": {
        "pre_actions": [
            "{initiator} is calmly shaving their arm hair to their preferred length while in the shower."
        ]
    },
    "mixer_social_WooHooFerrisWheel_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a romantic and intimate activity as they are WooHooing on the Ferris Wheel, taking their relationship to a new level."
        ]
    },
    "mixer_social_WooHooHauntedHouse_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a passionate encounter in the haunted house, as they are taking their relationship to the next level."
        ]
    },
    "mixer_social_WooHooTunnelLove_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are passionately engaging in a romantic rendezvous, embracing in the Tunnel of Love."
        ]
    },
    "mixer_Social_Fear_Failing_Class_AskForExtraCredit": {
        "pre_actions": [
            "{initiator} is approaching {target} and nervously asking if there is any chance for extra credit in order to avoid failing the class."
        ]
    },
    "mixer_social_WooHooPhotobooth_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into a photo booth together and engaging in a steamy WooHoo session."
        ]
    },
    "mixer_Shower_Shave_Back": {
        "pre_actions": [
            "{initiator} is asking {target} for help to shave their back hair while they are in the shower."
        ]
    },
    "mixer_Shower_Shave_Back_Passive": {
        "pre_actions": [
            "{initiator} is asking {target} for help in shaving their back hair while they are both taking a shower."
        ]
    },
    "mixer_Shower_Shave_Back_Preferred": {
        "pre_actions": [
            "{initiator} is going into the shower and shaving their back hair to their preferred length."
        ]
    },
    "mixer_Shower_Shave_Back_Preferred_Passive": {
        "pre_actions": [
            "{initiator} is using a shower to shave their back hair to their preferred length in a passive manner."
        ]
    },
    "mixer_Social_TryForBabyInPhotobooth_targeted_romance_transition": {
        "pre_actions": [
            "{initiator} and {target} are sneaking into the photo booth together, hoping to start a family and take their relationship to the next level."
        ]
    },
    "mixer_socials_SwapBabyMilestoneStories_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is approaching {target} and excitedly suggesting swapping baby milestone stories, wanting to share experiences and bond over their shared journey of parenthood."
        ]
    },
    "mixer_socials_TalkAboutSibling_Targeted_Friendly_AlwaysOn_STC_Child": {
        "pre_actions": [
            "{initiator} is engaging in a friendly conversation with {target}, talking about their siblings."
        ]
    },
    "mixer_Social_BabyShower_AskIfExcitedToBeSibling": {
        "pre_actions": [
            "{initiator} is approaching {target} at the baby shower and asking if they are excited to become a big sibling."
        ]
    },
    "mixer_social_BayArea_NPC_baygossip_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is taking {target} aside and sharing some juicy secrets about San Sequoia, a popular destination in the Bay Area. They are engaging in a targeted and friendly conversation."
        ]
    },
    "mixer_Social_BabyShower_CongratulateHost": {
        "pre_actions": [
            "{initiator} is attending the baby shower and congratulating the host, {target}."
        ]
    },
    "mixer_Social_BabyShower_SuggestBabyName": {
        "pre_actions": [
            "{initiator} is approaching {target} at the baby shower and suggesting a baby name."
        ]
    },
    "mixer_Social_BabyShower_Gush": {
        "pre_actions": [
            "{initiator} is excitedly gushing to {target} about the new baby and their upcoming baby shower."
        ]
    },
    "mixer_Social_BabyShower_GuessBabyFuture": {
        "pre_actions": [
            "{initiator} is attending a baby shower and engaging in conversation, guessing what future career the new baby may have."
        ]
    },
    "mixer_Social_BabyShower_OfferParentAdvice": {
        "pre_actions": [
            "{initiator} is attending a baby shower and offering the new parents some parenting advice."
        ]
    },
    "mixer_Social_BabyShower_AskIfExcitedToBeSibling_Toddler": {
        "pre_actions": [
            "{initiator} is approaching {target} at the baby shower and asking them if they are excited to be a big sibling, considering the presence of toddlers."
        ]
    },
    "mixer_social_ComplainAboutBurnout": {
        "pre_actions": [
            "{initiator} is venting to {target} about feeling burnt out and overwhelmed."
        ]
    },
    "mixer_social_ComplainAboutBurnout_Fog": {
        "pre_actions": [
            "{initiator} is voicing their frustration to {target} about feeling burnt out, feeling overwhelmed by the fog."
        ]
    },
    "mixer_Social_JobLoss_AskAboutJobLoss": {
        "pre_actions": [
            "{initiator} is asking {target} about their recent job loss."
        ]
    },
    "mixer_Social_JobLoss_ConsoleAboutJobLoss": {
        "pre_actions": [
            "{initiator} is consoling {target} about their recent job loss, offering support and understanding during this difficult time."
        ]
    },
    "mixer_Social_JobLoss_CongratulateOnNewJob": {
        "pre_actions": [
            "{initiator} is congratulating {target} on their new job."
        ]
    },
    "mixer_social_LifeMilestone_TellEpicTales": {
        "pre_actions": [
            "{initiator} is regaling {target} with epic tales from {initiator}'s life, sharing memorable experiences and achievements."
        ]
    },
    "mixer_social_WelcomeToHousehold_Friendly": {
        "pre_actions": [
            "{initiator} is warmly welcoming {target} to the household."
        ]
    },
    "mixer_Social_TryForBabyAsk_Treehouse": {
        "pre_actions": [
            "{initiator} is inviting {target} into the treehouse and suggesting they try for a baby together."
        ]
    },
    "mixer_Social_WooHooAsk_Treehouse": {
        "pre_actions": [
            "{initiator} is asking {target} if they want to have some fun and WooHoo in the treehouse."
        ]
    },
    "mixer_social_familytrope_CheerUp_targeted_friendly_emotionSpecific": {
        "pre_actions": [
            "{initiator} is trying to cheer up their family member, {target}, by offering words of encouragement and support."
        ]
    },
    "mixer_Social_SleepingBag_AskToPillowFight": {
        "pre_actions": [
            "{initiator} is inviting {target} to a pillow fight, playfully challenging them to a friendly and fun competition."
        ]
    },
    "mixer_social_Toddler_Mean_CrossAge_Interactions_Kick": {
        "pre_actions": [
            "{initiator} is kicking {target} in a mean-spirited act, despite the age difference."
        ]
    },
    "mixer_socials_Toddler_TalkAbouts_CrossAge_Interactions_FavoriteShow": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} about their favorite show, bridging the age gap between them."
        ]
    },
    "mixer_socials_Toddler_TalkAbouts_CrossAge_Interactions_FavoriteGame": {
        "pre_actions": [
            "{initiator} is initiating a conversation with {target}, discussing their favorite game. Despite the age difference, they are engaging in a friendly interaction about their shared interest in gaming."
        ]
    },
    "mixer_socials_Toddler_TalkAbouts_CrossAge_Interactions_FavoriteFood": {
        "pre_actions": [
            "{initiator} is engaging in a conversation with {target} to discuss their favorite foods."
        ]
    },
    "mixer_socials_Toddler_Friendly_CrossAge_Interactions_SingSong": {
        "pre_actions": [
            "{initiator}, a toddler Sim, is initiating a social interaction with {target}, and is starting to sing a song together with them in a friendly cross-age interaction."
        ]
    },
    "mixer_socials_Toddler_Friendly_CrossAge_Interactions_Reassure": {
        "pre_actions": [
            "{initiator} is offering words of comfort and reassurance to {target} in a friendly and supportive manner, bridging the age gap."
        ]
    },
    "mixer_Social_MidlifeCrisis_StressAboutLostTime_SadTalk": {
        "pre_actions": [
            "{initiator} is expressing their concern about lost time to {target}, feeling stressed about reaching midlife and having a sad talk."
        ]
    },
    "mixer_Social_MidlifeCrisis_StressAboutLostTime_SadReact": {
        "pre_actions": [
            "{initiator} is expressing their stress about lost time to {target}, possibly due to a midlife crisis, resulting in a sad reaction."
        ]
    },
    "mixer_Social_FriendshipBracelet_FistBump": {
        "pre_actions": [
            "{initiator} and {target} are exchanging a friendly fist bump, solidifying their friendship."
        ]
    },
    "mixer_social_Fight_targeted_TemporaryStay": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a heated argument, resulting in a fight."
        ]
    },
    "mixer_Social_FriendshipBracelet_DemandBack": {
        "pre_actions": [
            "{initiator} is confronting {target} and demanding their friendship bracelet back."
        ]
    },
    "mixer_infant_WiggleToMusic_Anticipation_Big": {
        "pre_actions": [
            "{initiator}, an infant, is wiggling in anticipation as they are reaching a milestone, under the watchful eye of {target}."
        ]
    },
    "mixer_infant_WiggleToMusic_Anticipation_Small": {
        "pre_actions": [
            "The infant is wiggling to the music with anticipation, reaching a milestone."
        ]
    },
    "mixer_social_Hug_Friendly_Middlescore_BestHugEver": {
        "pre_actions": [
            "{initiator} is giving {target} the best hug ever, showing their friendly and affectionate nature."
        ]
    },
    "mixer_social_Hug_Friendly_Middlescore_AdoptionContinuation_CT": {
        "pre_actions": [
            "{initiator} is embracing {target} in a warm and friendly hug, deepening their bond."
        ]
    },
    "mixer_social_trait_HorseLover_ShareDetailedHorseFacts_targeted_Friendly_alwaysOn_child": {
        "pre_actions": [
            "{initiator}, a child Sim and Horse Lover trait, is excitedly approaching {target} and is beginning to share detailed horse facts in a friendly and enthusiastic manner."
        ]
    },
    "mixer_socials_TellJoke_group_Funny_alwaysOn_TellJokeAboutHorseOfCourse_trait_HorseLover": {
        "pre_actions": [
            "{initiator} is telling a funny joke about horses to a group, particularly targeting {target}, who is known to be a horse lover."
        ]
    },
    "Mixer_social_TellJoke_group_Funny_alwaysOn_child_HorseLover_TellJokeAboutHorseButts": {
        "pre_actions": [
            "{initiator} is joining a mixer group and deciding to tell a funny joke to brighten everyone's day. They are specifically choosing a joke about horse butts, knowing that {target} is a horse lover and will appreciate the humor."
        ]
    },
    "mixer_social_BragAboutRanching_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is excitedly talking about their ranch to {target}, wanting to share their accomplishments and knowledge in a friendly manner."
        ]
    },
    "mixer_social_HeartfeltCompliment_targeted_friendly_RanchNectar_werewolfTrash": {
        "pre_actions": [
            "{initiator} is kindly complimenting {target} on their unique taste in trash nectar, despite the strong odor."
        ]
    },
    "mixer_Social_CountryDancing_AskToDance": {
        "pre_actions": [
            "{initiator} is asking {target} if they want to join them in a country dance."
        ]
    },
    "mixer_social_HowdyIntroduction_greetings": {
        "pre_actions": [
            "{initiator} is greeting {target} with a friendly 'Howdy' to introduce themselves."
        ]
    },
    "mixer_social_ShareStableGossip": {
        "pre_actions": [
            "{initiator} is sharing a juicy piece of gossip about the stable with {target}."
        ]
    },
    "mixer_Social_Toddler_BabbleToHorse": {
        "pre_actions": [
            "{initiator} is excitedly babbling to {target}, pretending to be having a conversation with a horse."
        ]
    },
    "mixer_Push_HorseToHorse_Touching_Groom": {
        "pre_actions": [
            "{initiator} is carefully pushing the horse closer to {target} and is beginning to groom it, gently touching and caring for its coat."
        ]
    },
    "mixer_Push_HorseToHorse_Touching_Sniff": {
        "pre_actions": [
            "{initiator} is approaching {target} and starting to sniff them, as a part of a debugging process."
        ]
    },
    "mixer_Push_HorseToHorse_Touching_Nuzzle": {
        "pre_actions": [
            "{initiator} is playfully nudging {target} with their nose in a friendly and affectionate manner."
        ]
    },
    "mixer_social_AnnounceEngagement": {
        "pre_actions": [
            "{initiator} is excitedly announcing their engagement to {target}."
        ]
    },
    "mixer_social_EnthuseAboutWedding": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about an upcoming wedding, sharing all the details and expressing their enthusiasm."
        ]
    },
    "mixer_social_ExpressDoubtsMarriage": {
        "pre_actions": [
            "{initiator} is expressing doubts about their impending marriage to {target}."
        ]
    },
    "mixer_social_CongratulateEngagement": {
        "pre_actions": [
            "{initiator} is congratulating {target} on their engagement."
        ]
    },
    "mixer_social_CongratulateMarriage": {
        "pre_actions": [
            "{initiator} is congratulating {target} on their recent marriage."
        ]
    },
    "mixer_social_JokeAboutMarriage": {
        "pre_actions": [
            "{initiator} is making a playful joke about marriage to {target}."
        ]
    },
    "mixer_social_AdmireNewlyweds": {
        "pre_actions": [
            "{initiator} is admiring the newlyweds, expressing their happiness for their union."
        ]
    },
    "mixer_social_GazeLovinglyNewlywed": {
        "pre_actions": [
            "{initiator} is lovingly gazing at their new spouse, admiring them with affection."
        ]
    },
    "mixer_social_AskToBeHonorAttendant": {
        "pre_actions": [
            "{initiator} is asking {target} if they can be the Sim of Honor at their wedding."
        ]
    },
    "mixer_social_AskForBlessingToMarry": {
        "pre_actions": [
            "{initiator} is gathering the courage to approach {target} and ask for their blessing to marry."
        ]
    },
    "mixer_social_Wedding_WeddingTradition_AskWeddingParty": {
        "pre_actions": [
            "{initiator} is asking {target} to be their Sim of Honor for the wedding, following the wedding tradition of asking close friends or family members to join the wedding party."
        ]
    },
    "mixer_social_Wedding_WeddingTradition_AskToComeToWedding": {
        "pre_actions": [
            "{initiator} is approaching {target} and politely asking if they can be invited to {1.SimFirstName}'s wedding."
        ]
    },
    "mixer_social_Wedding_Bouquet_AskAbout": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking about the flower bouquet, curious if it is for a wedding."
        ]
    },
    "mixer_social_Wedding_Bouquet_AngerOverToss": {
        "pre_actions": [
            "{initiator} is confronting {target} in anger over the bouquet toss incident on their wedding day."
        ]
    },
    "mixer_social_Wedding_Bouquet_JoyOverToss": {
        "pre_actions": [
            "{initiator} is excitedly cheering as {target} is catching the bouquet during the wedding day bouquet toss, expressing joy over the moment."
        ]
    },
    "mixer_social_WeddingToast_AskToMakeToast": {
        "pre_actions": [
            "{initiator} is approaching {target} and kindly asking if they can make a wedding toast."
        ]
    },
    "mixer_social_WeddingWorld_NPC_GrapevineGossip_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is excitedly sharing some wedding-related gossip with {target}, hoping to spread the news and engage in a friendly conversation."
        ]
    },
    "mixer_Social_PurchaseWeddingCake": {
        "pre_actions": [
            "{initiator} is going to the bakery to purchase a wedding cake for their upcoming nuptials."
        ]
    },
    "mixer_social_AskToBeFlowerSpreader": {
        "pre_actions": [
            "{initiator} is asking {target} if they can be the flower spreader at the wedding."
        ]
    },
    "mixer_social_AskToBeRingBearer": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking if they can be the ring bearer at the wedding."
        ]
    },
    "mixer_social_AskToBeOfficiant": {
        "pre_actions": [
            "{initiator} is asking {target} if they can officiate at their wedding."
        ]
    },
    "mixer_social_ReminisceAboutWedding_targeted_Friendly_alwaysOn": {
        "pre_actions": [
            "{initiator} and {target} are sharing memories and reminiscing about their wedding day."
        ]
    },
    "mixer_social_AskToBeFlowerSpreader_ChildTarget": {
        "pre_actions": [
            "{initiator} is excitedly asking the child, {target}, if they can be the flower spreader at the wedding."
        ]
    },
    "mixer_social_AskToBeRingBearer_ChildTarget": {
        "pre_actions": [
            "{initiator} is excitedly asking {target} if they can be the ring bearer at the wedding."
        ]
    },
    "mixer_social_EnthuseAboutWedding_ActorEngaged": {
        "pre_actions": [
            "{initiator} is excitedly talking to {target} about their upcoming wedding, sharing all the details and expressing their joy."
        ]
    },
    "mixer_social_JokeAboutMarriage_ActorEngaged": {
        "pre_actions": [
            "{initiator} is playfully making a joke about marriage to {target}, showing off their comedic side."
        ]
    },
    "mixer_social_FriendlyIntroduction_greetings_Werewolf": {
        "pre_actions": [
            "{initiator} is sniffing {target} curiously before introducing themselves in a friendly manner. Since {initiator} is a werewolf, this is their way of getting to know others."
        ]
    },
    "mixer_social_GossipAbout_targeted_friendly_alwaysOn_Werewolf": {
        "pre_actions": [
            "{initiator} is engaging in friendly conversation with {target}, but can't help but is spreading beastly rumors about the target being a werewolf."
        ]
    },
    "mixer_socials_TellJoke_group_Funny_alwaysOn_Werewolf": {
        "pre_actions": [
            "{initiator} is telling a funny joke about werewolves to {target} and their group, hoping to make them all laugh."
        ]
    },
    "mixer_social_WhisperSeductively_targeted_romance_middleScore_Werewolf": {
        "pre_actions": [
            "{initiator} is leaning in close to {target}, whispering seductively. Their eyes are glinting with a hint of mischief as they are trying to entice {target} with their werewolf charm."
        ]
    },
    "mixer_social_Insult_Mean_STC_Werewolf": {
        "pre_actions": [
            "{initiator} is mocking {target}'s feeble nature, making mean-spirited comments about their weakness. This interaction could be happening if {target} is a werewolf."
        ]
    },
    "mixer_social_YellAT_targeted_mean_Werewolf": {
        "pre_actions": [
            "{initiator}, a mean Werewolf, is aggressively snarling at {target} and yelling at them."
        ]
    },
    "mixer_Social_WerewolfPack_Discuss_PackA": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a discussion about the Moonwood Collective, a topic of interest within their werewolf pack."
        ]
    },
    "mixer_Social_WerewolfPack_PraiseValue_PackA": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their successful career in the werewolf pack, expressing admiration for their valued contributions."
        ]
    },
    "mixer_Social_WerewolfPack_ShareConcernsAboutGreg": {
        "pre_actions": [
            "{initiator} is confiding in {target} about their concerns regarding Greg's behavior within the Werewolf Pack."
        ]
    },
    "mixer_Social_WerewolfPack_DeclareSuperior_PackA": {
        "pre_actions": [
            "{initiator} is confidently declaring the Moonwood Collective as the superior werewolf pack to {target}, sparking a discussion about their respective strengths and abilities."
        ]
    },
    "mixer_Social_WerewolfPack_ComplainAbout_PackA": {
        "pre_actions": [
            "{initiator} is complaining to {target} about the Moonwood Collective, expressing frustration as a member of the Werewolf Pack."
        ]
    },
    "mixer_Social_WerewolfPack_ComplainAbout_PackB": {
        "pre_actions": [
            "{initiator} is complaining to {target} about The Wildfangs, expressing their displeasure about the werewolf pack."
        ]
    },
    "mixer_Social_WerewolfPack_DeclareSuperior_PackB": {
        "pre_actions": [
            "{initiator} is confidently declaring the Wildfangs as the superior werewolf pack to {target} during a spirited discussion."
        ]
    },
    "mixer_Social_WerewolfPack_PraiseValue_PackB": {
        "pre_actions": [
            "{initiator} is complimenting {target} on their career choice in the Werewolf Pack, showing appreciation for their value and dedication."
        ]
    },
    "mixer_Social_WerewolfPack_Discuss_PackB": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a discussion about the Wildfangs, sharing stories and information about their werewolf pack."
        ]
    },
    "mixer_Social_WerewolfPack_Mock_PackA": {
        "pre_actions": [
            "{initiator} is teasingly mocking the Moonwood Collective, likely provoking a reaction from them within their werewolf pack."
        ]
    },
    "mixer_Social_WerewolfPack_Mock_PackB": {
        "pre_actions": [
            "{initiator} is playfully mocking the Wildfangs, a friendly gesture among members of the Werewolf Pack."
        ]
    },
    "mixer_Social_WerewolfPack_AskAboutPacks_Region": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking about werewolf packs in the region."
        ]
    },
    "mixer_Social_WerewolfPack_AskAboutPacks_Member": {
        "pre_actions": [
            "{initiator} is asking {target} about werewolf packs and if they are a member of any."
        ]
    },
    "mixer_social_Fight_targeted_mean_WerewolfToSim": {
        "pre_actions": [
            "{initiator} is starting a fight with {target} after being provoked. The argument is quickly escalating to a physical confrontation as {1.SimFirstName} is using their werewolf powers."
        ]
    },
    "mixer_social_Fight_targeted_mean_SimToWerewolf": {
        "pre_actions": [
            "{initiator} is harshly confronting {target}, engaging in a fierce fight due to {initiator} being mean and {target} being a Werewolf."
        ]
    },
    "mixer_Social_Targeted_Friendly_AlwaysOn_Werewolf_AskToSpar": {
        "pre_actions": [
            "{initiator} is approaching {target} and is friendly asking if they would like to spar, as they are both sharing the werewolf trait."
        ]
    },
    "mixer_Social_Targeted_Friendly_AlwaysOn_Werewolf_AskToSpar_AtRing": {
        "pre_actions": [
            "{initiator} is approaching {target} at the Sparring Grounds, asking them to spar. They are engaging in a friendly werewolf spar at the ring."
        ]
    },
    "mixer_social_Fight_targeted_mean_WerewolfToWerewolf_Start": {
        "pre_actions": [
            "{initiator} and {target}, both werewolves, are engaging in a fierce brawl, fueled by their mean temperament and their werewolf nature."
        ]
    },
    "mixer_social_Fight_targeted_mean_WerewolfToVampire_Start": {
        "pre_actions": [
            "{initiator}, a mean Werewolf, is starting a Supernatural Smackdown with {target}, a Vampire."
        ]
    },
    "mixer_social_Fight_targeted_mean_VampireToWerewolf_Start": {
        "pre_actions": [
            "{initiator}, a mean Vampire, is starting a supernatural smackdown with {target}, a Werewolf."
        ]
    },
    "mixer_social_WolfTown_TellAboutUnderground_Friendly_MiddleScore": {
        "pre_actions": [
            "{initiator} is excitedly telling {target} about the secret underground tunnels in WolfTown."
        ]
    },
    "mixer_social_AskAboutWolfTown_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} about Moonwood Mill, in a friendly and interested manner."
        ]
    },
    "mixer_Social_Targeted_Friendly_AlwaysOn_WerewolfPack_JoinTrial_AskToSpar": {
        "pre_actions": [
            "{initiator}, a member of the Werewolf Pack, is approaching {target} and asking them to join a trial spar in a friendly and targeted social interaction."
        ]
    },
    "mixer_Social_WerewolfPack_EndFeud": {
        "pre_actions": [
            "{initiator} is approaching {target} from the Werewolf Pack, hoping to end the feud between them."
        ]
    },
    "mixer_Social_WerewolfPack_EndAlliance": {
        "pre_actions": [
            "{initiator} is confronting {target} and declaring that their alliance with the Werewolf Pack is over."
        ]
    },
    "mixer_social_Fight_targeted_mean_WerewolfToSim_Start": {
        "pre_actions": [
            "{initiator} is starting a fight with {target}, being mean and aggressive like a werewolf."
        ]
    },
    "mixer_social_Fight_targeted_mean_SimToWerewolf_Start": {
        "pre_actions": [
            "{initiator} is starting a fight with {target}, being mean towards them in order to assert dominance."
        ]
    },
    "mixer_social_WhisperSeductively_targeted_romance_middleScore_Werewolf_F": {
        "pre_actions": [
            "{initiator} is whispering seductively to {target}, using a low, growling tone. The atmosphere is becoming charged with a hint of romance, especially considering {initiator}'s werewolf nature."
        ]
    },
    "mixer_Social_Targeted_Friendly_AlwaysOn_Werewolf_AskToSpar_Commanded": {
        "pre_actions": [
            "{initiator} is approaching {target} in a friendly manner, asking if they would like to spar. As a werewolf, {initiator} is able to command {target} to engage in a friendly sparring match."
        ]
    },
    "mixer_Social_WerewolfPack_PackMentor": {
        "pre_actions": [
            "{initiator} is offering to provide mentorship to {target} within their werewolf pack."
        ]
    },
    "mixer_social_AskAboutWerewolfInterest_Targeted_Friendly_AlwaysOn": {
        "pre_actions": [
            "{initiator} is asking {target} if they are interested in becoming a werewolf."
        ]
    },
    "mixer_socials_GiveTheWerewolfTalk_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is approaching {target} and engaging in a friendly conversation, specifically targeting the topic of werewolves to give them information and advice about it."
        ]
    },
    "mixer_socials_AskAboutWerewolf_Targeted_Friendly_AlwaysOn_STC": {
        "pre_actions": [
            "{initiator} is engaging {target} in a friendly conversation and is asking them about their experience being a werewolf."
        ]
    },
    "mixer_Social_WerewolfPack_DisciplineMember": {
        "pre_actions": [
            "{initiator} is assertively disciplining {target}, reminding them of their responsibilities as a member of the werewolf pack."
        ]
    },
    "mixer_Social_WerewolfPack_AskAboutRank": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking about their pack rank, wanting to learn more about their status within the werewolf pack."
        ]
    },
    "mixer_Social_WerewolfPack_AskToBePackMentored": {
        "pre_actions": [
            "{initiator} is approaching {target} and asking to be mentored in becoming a member of the werewolf pack."
        ]
    },
    "mixer_Social_Targeted_Friendly_AlwaysOn_Werewolf_AskToTugOfWar": {
        "pre_actions": [
            "{initiator} is cheerfully asking {target} if they want to engage in a friendly game of Tug of War, attempting to socialize and bond with them."
        ]
    },
    "mixer_social_Fight_targeted_mean_WerewolfToSim_Start_Rampage": {
        "pre_actions": [
            "{initiator} is starting a fight with {target}, unleashing their mean side and causing chaos as a werewolf."
        ]
    },
    "mixer_social_Fight_targeted_mean_WerewolfToVampire_Start_Rampage": {
        "pre_actions": [
            "{initiator} and {target} are engaging in a supernatural smackdown, as the werewolf and vampire are starting a rampage, fighting each other with a mean and aggressive attitude."
        ]
    },
    "mixer_social_Fight_targeted_mean_WerewolfToWerewolf_Start_Rampage": {
        "pre_actions": [
            "{initiator} and {target}, both werewolves, are starting a brutal fight, unleashing their rage and causing chaos."
        ]
    },
}

for description in interaction_descriptions:
    print(json.dumps({'key': description, 'value': interaction_descriptions[description]['pre_actions'][0]}))
