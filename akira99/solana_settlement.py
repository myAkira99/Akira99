"""Solana on-chain settlement."""
from dataclasses import dataclass
from typing import dict


@dataclass
class Settlement:
    """Settlement result."""
    winners: list[str]
    payouts: dict[str, float]
    txn_hash: str = "mock_txn"
    fee: float = 0.05


class SolanaSettler:
    """Settles bets on Solana."""
    
    def settle(self, winners: list[str], payout_map: dict[str, float]) -> Settlement:
        """Settle bets on Solana."""
        total_payout = sum(payout_map.values())
        fee = total_payout * 0.05
        
        return Settlement(
            winners=winners,
            payouts=payout_map,
            fee=fee
        )
