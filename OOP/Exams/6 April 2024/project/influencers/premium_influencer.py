from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


# an initial payment percentage of 85%.
class PremiumInfluencer(BaseInfluencer):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * 0.85

    @property
    def campaign_types(self):
        return {
            "HighBudgetCampaign": 1.5,
            "LowBudgetCampaign": 0.8
        }

    def reached_followers(self, campaign_type: str):
        return int((self.followers * self.engagement_rate) * self.campaign_types[campaign_type])
